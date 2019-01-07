from project import *
import unittest



###################
#TESTS SCHOOL INFORMATION

class TestSchoolInfo(unittest.TestCase):

    def test_basic_search(self):
        self.assertTrue(len(school_name_lst), 474)
        self.assertTrue(len(school_ranking_lst), 474)
        self.assertTrue(len(reading_score),474)
        self.assertTrue(len(math_score),474)

class Test_lists(unittest.TestCase):
    def test_school_name_lst(self):
      
        self.assertEqual(type(school_name_lst[0]), type(float()))
        self.assertEqual(type(school_name_lst), type([]))
        self.assertTrue(len(school_name_lst) > 1)


    def test_school_ranking_lst(self):
        self.assertEqual(type(school_ranking_lst[0]), type(float()))
        self.assertEqual(type(school_ranking_lst), type([]))
        self.assertTrue(len(school_ranking_lst) > 1)


    def test_reading_score(self):
        self.assertEqual(type(reading_score[0]), type(str()))
        self.assertEqual(type(reading_score), type([]))
        self.assertTrue(len(reading_score) > 1)

    def test_math_score(self):
        self.assertEqual(type(math_score[0]), type(str()))
        self.assertEqual(type(math_score), type([]))
        self.assertTrue(len(math_score) > 1)


############################################
### TEST DATA SOURCES

class TestNearbySearch(unittest.TestCase):

    def place_is_in_places_list(self, place_name, places_list):
        for p in places_list:
            print(p)
            if place_name == p:
                return True
        return False

    def test_nearby_search(self):

        place1 = school_location("STAGG")
        place2 = school_location("GLOBAL CITIZENSHIP")
        place3 = school_location("LOCKE A")

        #self.assertTrue(self.place_is_in_places_list("41.7589946,'\n',-87.6494037", place1))
        #self.assertTrue(self.place_is_in_places_list("41.8091565'\n'-87.7468693",place2))
        #self.assertTrue(self.place_is_in_places_list("41.9317953'\n'-87.7956842",place3))



class Test_crime_cache_exists(unittest.TestCase):
    def setUp(self):
        self.f = open("2018crime.csv")

    def test_file_contains_info(self):
        self.assertTrue(self.f != None)

    def tearDown(self):
        self.f.close()


class Test_crime_cache_headers(unittest.TestCase):
    def setUp(self):
        self.f = open("2018crime.csv")
        self.lines = self.f.readlines()
        self.f.close()
    def test_headers(self):
        self.assertTrue("arrest,beat,block,case_number,community_area,date,description,district,domestic,fbi_code,id,iucr,latitude,location,location_description,longitude,primary_type,updated_on,ward,x_coordinate,y_coordinate,year" in self.lines[0])



class Test_school_cache(unittest.TestCase):
    def setUp(self):
        self.f = open("school_cache.json")
        #self.lines = self.f.readlines()
        #self.f.close

    def test_file_exists(self):
        self.assertTrue(self.f.read())

    def test_file_contains_info(self):
        self.assertTrue(self.f != None)

    def tearDown(self):
        self.f.close()


####################################
### TEST PLOTLY


class TestMapping(unittest.TestCase):

    def test_plot_school_locations(self):
        try:
            plot_school_locations('2018')

        except:
            self.fail()


    def test_plot_school_locations_info(self):
        try:
            plot_school_locations('2018')
            self.assertEqual(type(name),type(str()))
            self.assertEqual(type(h_lat_list),type([]))

        except:
            self.fail()
        #self.assertTrue(type(h_lat_list),type([]))
        #self.assertTrue(list(h_lon_list),type)
        #self.assertTrue(list(lat_list))
        #self.assertTrue(list(lon_list))
        #self.assertTrue(list(name))



if __name__ == '__main__':
    unittest.main(verbosity=2)