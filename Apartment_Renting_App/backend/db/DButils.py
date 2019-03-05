from ..db.connection import conn, cursor

#user
def get_user(role, parameter):
    sql_str = "SELECT * from USER WHERE {} = %s".format(role)
    cursor.execute(sql_str, (parameter, ))
    return cursor.fetchone()

def login(username):
    sql_str = "SELECT * from USER WHERE username = %s"
    cursor.execute(sql_str, (username, ))
    return cursor.fetchone()

def signup(username, password, email, isStudent):
    sql_str = "INSERT INTO USER (username,password,email,isStudent) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql_str, (username, password, email, isStudent))
    conn.commit()



#listing
def get_all_listings():
    sql_str = "SELECT * from LISTINGS WHERE isAvailable = TRUE ORDER BY create_date"
    cursor.execute(sql_str)
    return cursor.fetchall()

def get_listings_by_userid(user_id):
    sql_str = "SELECT * from LISTINGS WHERE renter_id = %s AND isAvailable = TRUE ORDER BY create_date"
    cursor.execute(sql_str, (user_id, ))
    return cursor.fetchall()


def get_listing_by_houseid(house_id):
    sql_str = "SELECT * from LISTINGS WHERE house_id = %s AND isAvailable = TRUE ORDER BY create_date"
    cursor.execute(sql_str, (house_id, ))
    return cursor.fetchone()


def create_new_listing(user_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url):
    sql_str = "INSERT INTO LISTINGS (renter_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql_str, (user_id, house_name, price, size, distance, number, street, city, state, zipcode, image_url))
    conn.commit()


def delete_listing(house_id):
    sql_str = "DELETE from LISTINGS WHERE house_id = %s"
    cursor.execute(sql_str, (house_id, ))
    conn.commit()


#order
def get_orders_by_id(role, user_id):
    sql_str = "SELECT * from ORDERS WHERE {} = %s ORDER BY create_date".format(role)
    # print(sql_str, (user_id, ))
    cursor.execute(sql_str, (user_id, ))
    return cursor.fetchall()


# def get_orders_by_customerid(user_id):
#     sql_str = "SELECT * from ORDERS WHERE customer_id = %s ORDER BY create_date"
#     cursor.execute(sql_str, (user_id, ))
#     return cursor.fetchall()


def place_order(house_id, renter_id, customer_id):
    try:
        sql_str_order = "INSERT INTO ORDERS (house_id, renter_id, customer_id, create_date) VALUES (%s, %s, %s, NOW())"
        cursor.execute(sql_str_order, (house_id, renter_id, customer_id))
        sql_str_listings = "UPDATE LISTINGS SET isAvailable = %s WHERE house_id = %s"
        cursor.execute(sql_str_listings, (0, house_id))
        conn.commit()
    except:
        conn.rollback()

#message

def get_all_msg_by_id(role, user_id):
    sql_str = "SELECT * from MESSAGE WHERE {} = %s ORDER BY date".format(role)
    # print(sql_str, (user_id, ))
    cursor.execute(sql_str, (user_id,))
    return cursor.fetchall()


def get_msg_detail(renter_id, customer_id):
    sql_str = "SELECT * from MESSAGE WHERE renter_id = %s AND customer_id = %s ORDER BY date"
    cursor.execute(sql_str, (renter_id, customer_id))
    return cursor.fetchall()


def send_msg(renter_id, customer_id, msg):
    sql_str = "INSERT INTO MESSAGE (renter_id, customer_id, message, date) VALUES (%s, %s, %s, NOW())"
    cursor.execute(sql_str, (renter_id, customer_id, msg))
    conn.commit()





