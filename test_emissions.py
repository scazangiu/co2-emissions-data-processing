import unittest
import os
from proj2 import Row, Node, read_csv_lines, listlen, filter_rows, parse_row


class TestProject2(unittest.TestCase):

    def setUp(self):
        self.filename = "test_emissions.csv"
        with open(self.filename, "w", newline="") as file:
            file.write(
                "country,year,electricity_and_heat_co2_emissions,"
                "electricity_and_heat_co2_emissions_per_capita,"
                "energy_co2_emissions,energy_co2_emissions_per_capita,"
                "total_co2_emissions_excluding_lucf,"
                "total_co2_emissions_excluding_lucf_per_capita\n"
                "USA,2000,100.0,1.0,200.0,2.0,300.0,3.0\n"
                "Canada,2001,50.0,,120.0,1.2,180.0,1.8\n"
                "Mexico,1999,,0.7,90.0,0.9,150.0,1.5\n"
            )

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_row_and_node(self):
        row = Row("USA", 2020, 1.0, None, 2.0, None, 3.0, None)
        node = Node(row, None)

        self.assertEqual(node.value.country, "USA")
        self.assertIsNone(node.next)

    def test_parse_row(self):
        row = parse_row(["Canada", "2001", "50.0", "", "120.0", "1.2", "180.0", "1.8"])

        self.assertEqual(row.country, "Canada")
        self.assertEqual(row.year, 2001)
        self.assertIsNone(row.electricity_and_heat_co2_emissions_per_capita)

    def test_read_csv_lines_and_listlen(self):
        data = read_csv_lines(self.filename)

        self.assertEqual(listlen(data), 3)
        self.assertEqual(data.value.country, "USA")

    def test_filter_rows_country(self):
        data = read_csv_lines(self.filename)
        filtered = filter_rows(data, "country", "equal", "USA")

        self.assertEqual(listlen(filtered), 1)
        self.assertEqual(filtered.value.country, "USA")

    def test_filter_rows_numeric(self):
        data = read_csv_lines(self.filename)
        filtered = filter_rows(data, "year", "greater_than", 1999)

        self.assertEqual(listlen(filtered), 2)


if __name__ == "__main__":
    unittest.main()
