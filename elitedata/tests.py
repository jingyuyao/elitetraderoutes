import time
from rest_framework.test import APITestCase

from .models import *

# Create your tests here.

class SystemTests(APITestCase):
    def setUp(self):
        self.now = int(time.time())
        System.objects.create(name="Sol", needs_permit=True, primary_economy='Industrial',
                              population=70000000, security="High", allegiance='Federation',
                              government='Anarchy', state='', faction='None',
                              x=100, y=100, z=100, updated_at=self.now)

    def test_system_properties(self):
        sol = System.objects.get(name='Sol')
        self.assertIsNotNone(sol)
        self.assertEqual(sol.name, 'Sol')
        self.assertEqual(sol.needs_permit, True)
        self.assertEqual(sol.primary_economy, 'Industrial')
        self.assertEqual(sol.population, 70000000)
        self.assertEqual(sol.security, 'High')
        self.assertEqual(sol.allegiance, 'Federation')
        self.assertEqual(sol.government, 'Anarchy')
        self.assertEqual(sol.state, '')
        self.assertEqual(sol.faction, 'None')
        self.assertEqual(sol.x, 100)
        self.assertEqual(sol.y, 100)
        self.assertEqual(sol.z, 100)
        self.assertEqual(sol.updated_at, self.now)
        self.assertFalse(sol.stations.exists())

    def test_system_station_relation(self):
        sol = System.objects.get(name='Sol')
        self.assertFalse(sol.stations.exists())
        station = Station.objects.create(name='Titan', system=sol, updated_at=self.now)
        self.assertTrue(sol.stations.exists())
        station.delete()
        self.assertFalse(sol.stations.exists())
