# DBMS-MINI-Project

1.	Introduction

We live in a culture where we want everything to be done as affordably as possible. When it comes to medical care for our families, most of the times the prices of the treatments are not affordable and it breaks the financial conditions or many a times is not affordable at all. The system will not only help to manage the inventory medicines but also suggest the alternative generic medicines at the same time.

1.1	Mini Project Statement

Hospitals have inventories where they store the medicines. Hospitals have unique ID of the branch, location, and name. These medicines are used for treating the patients and are also sold in the pharmacy of the hospital too. The medicines have Name, registration number for unique identification and to verify if the medicine is actually approved by the DCA, Total quantity, Date of manufacture, Best before, Manufacturer, price, priority level(If the medicines are to be sold/given only if there is a prescription for it). The same medicines can be ordered multiple times therefore the dates have to be kept for each batch of medicines.  Every Inventory has a unique number, type (cold storage, normal, and hybrid) and location in the hospital. The inventory staff has the responsibility of taking out the medicines from the inventory and updating it in the list. There are 3 staff members assigned to every inventory of which one of them is the head (self-relation) for other members. Every staff has a unique id, name, phone number, address and start date. The system will give a prompt to the staff if any of the medicines in the inventory are near the expiration date. The system will also generate a prompt if any of the medicines go below the minimum stock level so that they can be ordered in time for the patient's smooth treatment. We have the information about the diseases which are identified by an ID, name, and the best medicine to treat it is linked to the disease. The system will give information about some of the top medicines sorted in descending order of price in which the major components of the medicine are same to the medicine best suitable to treat that disease. It would be helpful to the people who cannot afford the costly medicines but the generic medicines would give them some hope without ruining their financial condition.

1.2	Area

The area of working for this system is medical facilities as well as public welfare.

1.3	Mini Project Aim

The main aim of this system is to help people get the right medicine if the ones prescribed are not affordable by them. In addition to that the system also helps in managing the medicines in the hospital’s inventories.

1.4 Applications

This system is applicable in every hospital which has inventories for storing medicines. It would be helpful as it makes the system more easy to use for the staff working at the hospitals. This system also has an option to find alternatives for medicines if the person is unable to afford that particular medicine and this can be applicable at every hospital for people. 
2.	Background Work

We had been involved in on field result by visiting various medical stores and consulting them regarding our project and how they are able to keep a well-maintained record of the stocks of medicines and how the order is placed according to the demand. It helped us to provide a clear mindset on how carry forward our project.
3.	Problem Statement

3.1 Mini Project Scope

The scope of our project is to provide an easy and interactive GUI for inventory to easily process orders of the medicines and to suggest the best medicine available to the user for the particular disease.

3.2	Mini Project Assumptions

The inventory is associated with a particular hospital is independently managed by that hospital only. The price of the medicines is been fixed are not supposed to change in shorter duration of time.

3.3	Mini Project Limitations

It can be used to provide the best medicines for only the disease which are already been stored in the database. For any new disease found we need to provide first the information about the disease and the medicines suitable for it. Also the system can right now classify medicines which have only one component in their composition.

3.4	Use Case Diagram
 

 

3.5	E-R Diagram

 

Erd to Schema 
 

3.6	Reduction Of ERD into Tables
 

Diseases table

 

Hospital table

 
Medicines table
 

Medicines_chemicals Table
 

Medicines_order_details Table
 




Staff Table
 


Temp table made through our procedure

 



3.7	Normalization

The tables have been normalized to 3NF.

4.	Mini Project Requirements

4.1 Software Requirements

We need any code editor such as VSCode, PyCharm for writing and editing the code and for building our app which will be used to run and deploy aur application on the webserver.
We need to install python in the PC as we had used python as the programming language along with it we need to import mysql Connector for establishing connections and Flask lib., their specific classes to build our application and to make route connection.
We need mysql to be install in the PC in order to store the data which is being generated, Processed and been retrieved to our web application. It has been used as it provide flexibility, reliability and speed.


4.2	Hardware Requirements

We need an PC on which our application will be running. We need fast internet connection so that the request and response mechanism between client and server is established strongly. Our system requires sufficient memory space in order to store the data.

4.3	SQL Query Statements

1) To write a query to place order for the particular inventory
          Select * from medicines;
2) To write a query to update the quantity of the particular record
        Update medicines set quantity=up_qtywhrebatch_no=B_no;
3) To write a query to Delete the order placed on the basis of the batch number
        Delete from medicines where batch_no=B_no;
4) To write a query to display the order details which are been placed by the inventory.
        Select * from medicines;

4.4	PL/SQL Query Statements

1) To write a procedure to find the name of medicine for the particular disease, their price and order them according to the price.
mysql> CREATE PROCEDURE best_opt1(disease VARCHAR(20))
    BEGIN
    DECLARE b_medVARCHAR(50) DEFAULT bmed(disease);
    DECLARE b_med_chemVARCHAR(50) DEFAULT chem(bmed(disease));
    DECLARE n VARCHAR(50);
    DECLARE med_forVARCHAR(20);
    DECLARE p float;
    DECLARE done INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT  m.Name,m.M_D_name,m.price FROM medicines m INNER JOIN medicines_chemicals mc ON m.Name=mc.M_Name AND M_D_name=disease ORDER BY Chemical_name_and_composition=b_med_chemDESC,price;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done=1;
    OPEN cur;
    REPEAT
    FETCH cur INTO n,med_for,p;
    IF done=0 THEN
    INSERT INTO temp VALUES(n,med_for,p);
    END IF;
    UNTIL done END REPEAT;
    CLOSE cur;
    END;
    $$
2) To write a function to find the best medicine for the particular disease.
mysql> CREATE FUNCTION bmed(disease VARCHAR(20)) RETURNS VARCHAR(50)
    -> DETERMINISTIC
    -> BEGIN
    -> DECLARE bestmedVARCHAR(50);
    -> SELECT best_med INTO bestmed FROM diseases WHERE D_name=disease;
    -> RETURN bestmed;
    -> END;
    -> $$
Query OK, 0 rows affected (0.13 sec)

3) To write a function to find the chemical composition of the medicine when the name of the medicine is specified as the parameter passing through it.
mysql> CREATE FUNCTION chem(medicine VARCHAR(50)) RETURNS VARCHAR(50)
    -> DETERMINISTIC
    -> BEGIN
    -> DECLARE chemcompVARCHAR(50);
    -> SELECT Chemical_name_and_composition INTO chemcomp FROM medicines_chemicals WHERE M_Name=medicine;
    -> RETURN chemcomp;
    -> END;
    -> $$
Query OK, 0 rows affected (0.13 sec)

5	Conclusion

Thus we had tried to build an web application which is able to assist the Hospital inventory is able to recommend them with the best medicines available for the particular medicine and Thus, it reduces human efforts and increases the efficiency of the hospital

.

6	References

https://flask.palletsprojects.com/en/2.2.x/
https://www.w3schools.com/python/python_mysql_getstarted.asp
https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
https://stackoverflow.com/questions/69685885/capturing-mysql-connection-error-in-python
https://getbootstrap.com/docs/4.1/content/tables/

