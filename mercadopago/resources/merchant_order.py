from mercadopago.core import MPBase

class MerchantOrder(MPBase):

    """
    This class will allow you to create and manage your orders. You can attach one or more payments in your merchant order.
    """
    
    def __init__(self, request_options, http_client):
        super(MerchantOrder, self).__init__(request_options, http_client)

    def search(self, filters, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/merchant_orders/_merchant_orders_search/get/)

        Args:
            filters (dict): The search filters parameters
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Merchant Order find response
        """
        return self._get(uri="/merchant_orders/search", filters=filters, request_options=request_options)

    def get(self, id, request_options=None):  
        """[Click here for more infos](https://www.mercadopago.com/developers/en/reference/cards/_customers_customer_id_cards/get/)

        Args:
            id (str): The Merchant Order ID
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Returns:
            dict: Cards find response
        """
        return self._get(uri="/merchant_orders/" + str(id), request_options=request_options)

    def update(self, id, merchant_order_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/merchant_orders/_merchant_orders_id/put/)

        Args:
            id (str): Merchant Order ID 
            merchant_order_object (dict): Merchant Order object to be updated
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
            ValueError: Param merchant_order_object must be a Dictionary     
        Returns:
            dict: Cards modification response
        """
        if type(merchant_order_object) is not dict:
            raise ValueError('Param merchant_order_object must be a Dictionary')

        return self._put(uri="/merchant_orders/" + str(id), data=merchant_order_object, request_options=request_options)

    def create(self, merchant_order_object, request_options=None):
        """[Click here for more infos](https://www.mercadopago.com.br/developers/en/reference/merchant_orders/_merchant_orders/post/)

        Args:
            merchant_order_object (dict): Merchant Order object to be created
            request_options (mercadopago.config.request_options, optional): An instance of RequestOptions can be pass changing or adding custom options to ur REST call. Defaults to None.

        Raises: 
            ValueError: Param merchant_order_object must be a Dictionary     
        Returns:
            dict: Cards creation response
        """
        if type(merchant_order_object) is not dict:
            raise ValueError('Param merchant_order_object must be a Dictionary')

        return self._post(uri="/merchant_orders", data=merchant_order_object, request_options=request_options)
