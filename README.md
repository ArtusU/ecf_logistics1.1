# ecf_logistics1.1

This Django App allows to collect the orders by the Users and display and organise them by the Admin.

![image](https://drive.google.com/uc?export=view&id=1fyMXyetPqv-ume2-R9H_Z5NpjQM5mtxY)

### The referrer - default user
The referrer can sign up to the service themselves or could be registered by authorised institution for example Local Council. 
The Referrers, usually Social Workers or NHS Nurses can log in to the service and refer a participant for a free fruit&veg box delivered by the local charity. 

![image](https://drive.google.com/uc?export=view&id=1AOGrjwXn6X88DcEWi1u0kYmRo0wEEDNa)

After Login the referrer can see the list of the previously referred participants and access the individual detail view. 

![image](https://drive.google.com/uc?export=view&id=1SGEWCSW2JrNsn0FZSzi5-UCf5_zAyO8L)

The referrer can also edit their own details. 

![image](https://drive.google.com/uc?export=view&id=1exMVCAJUbrgm3pkT6BwAac2kwFkCRnpV)

The referrer can place an order by filling the form with participants' details 

![image](https://drive.google.com/uc?export=view&id=19yV7gxb-mkGLVQ6bCVINaCBpxsfj1l9u)


### The Warehouse Admin - admin user.
The local charity's Warehouse Admin has the full view of the received orders.  

![image](https://drive.google.com/uc?export=view&id=19NKeWV6QfMZYZyY_BphR3hd9MnuZYi_E)

In the process of organising deliveries, the admin can stage the orders assigning: 
* status (approved, pending, out of delivery, delivered),
* delivery day (from Monday to Friday),
* delivery run (from 1 to 5).

![image](https://drive.google.com/uc?export=view&id=1tHvM8reN9SZVT9Bh9mDinr5BAYioGDYe)
	
The Admin has full sorting functionality available:
* by the referrer surname and institution,
* by the recipient full name,
* by the product, order status, delivery day, and run. 

![image](https://drive.google.com/uc?export=view&id=1IJSsMD2wzHgJlB1_nkYyuP8Ct4vbKhN5)

### The driver - staff user.
The five drivers can log in to the service. The dashboard shows all the orders staged by the Warehouse Admin as 'out of delivery'.  The drivers can sort out the run (from 1 to 5) and delivery day. If needed they have full access to the order details.

![image](https://drive.google.com/uc?export=view&id=1PVg3j3lKFkInu1oRc_-zbpisymRUN4NB)

https://ecfcrm.herokuapp.com/
