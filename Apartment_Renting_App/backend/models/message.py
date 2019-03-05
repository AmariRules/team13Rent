from ..db import DButils


def get_msg_by_customerid(customer_id):
    all_msg = DButils.get_all_msg_by_id("customer_id", customer_id)
    renter_id_set = []
    for msg in all_msg:
        renter_id_set.append(msg[0])
    renter_username = []
    for renter_id in renter_id_set:
        renter = DButils.get_user("user_id", renter_id)
        renter_username.append(renter[1])
    return renter_username


def get_msg_by_renterid(renter_id):
    all_msg = DButils.get_all_msg_by_id("renter_id", renter_id)
    customer_id_set = []
    for msg in all_msg:
        customer_id_set.append(msg[0])
    customer_username = []
    for renter_id in customer_id_set:
        renter = DButils.get_user("user_id", renter_id)
        customer_username.append(renter[1])
    return customer_username


def get_msg_detail(renter_id, customer_id):
    return DButils.get_msg_detail(renter_id, customer_id)



def send_msg(renter_id, customer_id, msg):
    DButils.send_msg(renter_id, customer_id, msg)

#
#
# def send_msg_from_dashboard()