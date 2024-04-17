
# APICOnstants- class which contain all the endpoints
# we will keep the urls here


class APIConstants(object):

    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com/"

    # static method can be called without the object .You can call it directly by using class.


    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"


    # update ,put,patch,delete - bookingId

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

