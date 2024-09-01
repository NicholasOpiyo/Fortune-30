from django.test import TestCase, Client
from django.urls import reverse

from top30profiles.views import get_sectors

class Fortune30Tests(TestCase):
    def test_client(self):
        self.client = Client()
    # Testing the 'index' endpoint
    def test_index_route(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
    # Testing the 'industries' endpoint
    def test_industries_route(self):
        response = self.client.get(reverse("all industries"))
        self.assertEqual(response.status_code, 200)
    # Testing the 'specific industry' endpoints
    def test_specific_industries_routes(self):
        # Obtaining the list of endpoints
        all_sectors = get_sectors()
        # Creating list for tracking succesful requests
        successes = []
        # Making post requests and tracking responses
        for s in all_sectors:
            route_to_test = '/industries/' + s
            response = self.client.post(route_to_test, {'industry': s})
            if response.status_code == 200:
               successes.append(200)
        # Testing the equality of succesful requests and the number of endpoints    
        self.assertEqual(len(all_sectors), len(successes))

    



