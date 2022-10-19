class Orders:

    def __init__(self):
        self.number_of_trips = 1
        self.current_order_amount_list = []

    def combine_orders(self, requests, n_max):
        """Returns an integer representing the minimum number of trips that must to be done based on criteria provided
        by institution.

        This method will first check if there is a request, and if the order_amount in that request is lower than
        n_max value.

        If those conditions are met, we will check if this order fits in current order request
        (self.current_order_amount_list)

        Please note that:

            - We can have a maximum number of 2 requests in an order request.
            - An order request cannot have the sum of amounts in the current request > n_max value

        This is handled by check_if_fits method, that will return a True or False flag.

        Case the flag is True, we will add the amount to the current order request.

        If the flag is False, we will reset the current order amount list, add +1 to trip counter
        and add the current order_amount to this request.
        """

        if requests:
            for order_amount in requests:
                if order_amount <= n_max:
                    order_amount_sum = self._get_order_amount_sum()
                    fit_flag = self._check_if_fits(order_amount_sum, order_amount, n_max)

                    if fit_flag is True:
                        self._add_order_amount(order_amount)

                    if fit_flag is False:
                        self._reset_order_amount_list()
                        self._add_trip()
                        self._add_order_amount(order_amount)

            return self.number_of_trips

        if not requests:
            return 0

    def _reset_order_amount_list(self):
        """Resets order amount list for a new trip"""

        self.current_order_amount_list = []

    def _add_order_amount(self, order_amount):
        """Add order amount to order list"""

        self.current_order_amount_list.append(order_amount)

    def _check_if_fits(self, order_amount_sum, order_amount, n_max):
        """Checks if order amount fits in current order list.

        This method will return a True of False flag depending on the following criteria:

        order_amount_sum + current order amount should be lower than n_max value

        Also, the number of requests in this order request is limited to 2 items.
        """

        total = order_amount_sum + order_amount

        if (total <= n_max) and (len(self.current_order_amount_list) < 2):
            return True

        if (total > n_max) or (len(self.current_order_amount_list) == 2):
            return False

    def _get_order_amount_sum(self):
        """Returns the sum of order amount values in current order amount list"""
        return sum(self.current_order_amount_list)

    def _add_trip(self):
        """Add one more trip to number_of_trips"""

        self.number_of_trips += 1
