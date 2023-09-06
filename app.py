from flask import Flask, render_template, request,redirect
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from database.dbConfig import databaseConnection
cursor,conn=databaseConnection()

app=Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)



# @app.route('/',methods=['GET','POST'])
# def index():
#     if request.method=='POST':
#         user=request.form
#         # cur=mysql.connection.cursor()
#         cursor.execute("select * from medicines")
#         data=cursor.fetchall()
#         print(data)
        
        
        
#         return redirect('/update')
        
    
#     return render_template('index.html')


# @app.route('/update',methods=['GET','POST'])
# def abc():
#     if request.method=='POST':
#         return "Siddharth"
#     return render_template('update.html')


@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        user=request.form
        # cur=mysql.connection.cursor()
        cursor.execute("select * from medicines")
        data=cursor.fetchall()
        print(data)
        
        
        
        return redirect('/options')
        
    
    return render_template('index.html')

@app.route('/options',methods=['GET','POST'])
def opt():
    if request.method=='POST':
        if request.form.get('insert')=='Place Order':
            return redirect('/insert')
        elif request.form.get('update')=='Update Order':
            return redirect('/update')
        elif request.form.get('delete')=='Delete Order':
            return redirect('/delete')
        elif request.form.get('display')=='Display Order':
            return redirect('/display')
        elif request.form.get('callp')=='Best Medicine List':
            return redirect('/pro')
        elif request.form.get('bestm')=='Best Medicine':
            return redirect('/f1')
        elif request.form.get('chemic')=='Chemical':
            return redirect('/f2')
       
            
    
    
    return render_template('page2.html')


@app.route('/display',methods=['GET','POST'])
def disp():
    cursor.execute("SELECT O_M_Name, O_quantity,batch_number from  medicines_order_details")
    
    medicine_detail=cursor.fetchall()
    
    if request.method=='POST':
        return redirect('/options')
    return render_template('output.html',data= medicine_detail)
    
@app.route('/insert',methods=['GET','POST'])
def abc():
    if request.method=='POST':
        # fetch the data
        userdetails=request.form
        name=userdetails['M_name']
        quant=userdetails['quantity']
        batch_num=userdetails['Batch_no']
        cursor.execute("INSERT INTO  medicines_order_details( O_M_Name, O_quantity,batch_number) values(%s,%s,%s)",(name,quant,batch_num))
        conn.commit()
        
        
        
        
        return  redirect('/display')
        
    return render_template('insert.html')    



@app.route('/update',methods=['GET','POST'])
def ac():
    if request.method=='POST':
        userdetails=request.form
        batch=userdetails['batch_number']
        quant=userdetails['quantity']
        cursor.execute("UPDATE medicines_order_details set  O_quantity=(%s) where batch_number=(%s)",(quant,batch))
        conn.commit()
        
        
        return  redirect('/display')
    return render_template('update.html')


@app.route('/delete',methods=['POST','GET'])
def xyz():
    if request.method=='POST':
        userdetails=request.form
        batch=userdetails['B_number']
        
        
        cursor.execute(f"DELETE from  medicines_order_details where batch_number={batch}")
        conn.commit()
        
        
        return  redirect('/display')
        
    return render_template('delete.html')  


# @app.route('/pro',methods=['POST','GET'])
# def call_procedure():
#     if request.method=='POST':
#         arg="Cancer"
#         result=cursor.callproc('best_opt1', arg)
#         print(result[1])
#         # result=cursor.callproc('best_opt1', arg)
#         # result=result.fetchall()
#         conn.commit()
#         # for i in result:
#         #     print(i)
#         # return result
#     return "the procedure is called"

@app.route('/pro',methods=['GET','POST'])
def call_procedure():
    arg=str('Cancer')
    # cursor.execute(f"CALL best_opt1({arg})")
    cursor.execute("CALL best_opt1((%s))",(arg,))
    conn.commit()
    cursor.execute("SELECT Name_of_med,Med_for,Price from temp")
    medicine_detail=cursor.fetchall()
    
    if request.method=='POST':
       
        if request.form.get('back')=='BACK':
            return redirect('/back_button')
        if request.form.get('main')=='MAIN':
                return  redirect('/options')
    
    return render_template('output1.html',data= medicine_detail)
        
        
        
        
   
        
  
@app.route('/back_button',methods=['GET','POST'])
def call_delete():
    
    cursor.execute("DELETE from  temp ")
    conn.commit()
    if request.method=='POST':
        if request.form.get('main')=='MAIN':
            return  redirect('/options')
        elif request.form.get('back')=='BACK':
            return render_template('output1.html')
        
    
    return render_template('output1.html')
    
@app.route('/f1',methods=['GET','POST'])
def fun1():
    if request.method=='POST':
        userdetails=request.form
        batch=userdetails['B_number']
        cursor.execute("SELECT bmed((%s)) as'The best medicine is'",(batch,))
        medicine_detail=cursor.fetchall()
        
    
        return render_template('outputfun1.html',data= medicine_detail)
    return  render_template('fun1.html')


@app.route('/f2',methods=['GET','POST'])
def fun2():
    if request.method=='POST':
        userdetails=request.form
        batch=userdetails['B_number']
        cursor.execute("SELECT chem((%s)) as'The Composition is as follows:- '",(batch,))
        medicine_detail=cursor.fetchall()
        
    
        return render_template('outputfun2.html',data= medicine_detail)
    return  render_template('fun2.html')


if __name__=="__main__":
    app.run(debug=True)