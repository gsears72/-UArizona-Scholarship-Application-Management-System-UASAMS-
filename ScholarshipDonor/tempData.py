
from .models import Scholarship
from .models import Donor

scholarship1 = Scholarship("Merit Scholarship", 5000, Donor("Donor1", "1234567890", "donor1@example.com"), 25000, 3.0, "Computer Science", "2023-01-15", [], [], "This scholarship recognizes outstanding academic achievement.")
scholarship2 = Scholarship("STEM Excellence Grant", 7000, Donor("Donor2", "9876543210", "donor2@example.com"), 30000, 3.2, "Engineering", "2022-11-20", [], [], "Awarded to students excelling in STEM fields.")
scholarship3 = Scholarship("Arts and Humanities Award", 4500, Donor("Donor3", "5555555555", "donor3@example.com"), 20000, 3.5, "Arts", "2023-03-05", [], [], "Recognizing achievements in the Arts and Humanities.")
scholarship4 = Scholarship("Community Service Scholarship", 6000, Donor("Donor4", "1111111111", "donor4@example.com"), 27000, 3.8, "Social Work", "2022-12-10", [], [], "For outstanding contributions to community service.")
scholarship5 = Scholarship("Innovation Fellowship", 8000, Donor("Donor5", "2222222222", "donor5@example.com"), 35000, 3.4, "Business", "2023-02-28", [], [], "Encouraging innovation and entrepreneurship.")
scholarship6 = Scholarship("Diversity and Inclusion Grant", 5500, Donor("Donor6", "3333333333", "donor6@example.com"), 28000, 3.2, "Psychology", "2022-12-01", [], [], "Promoting diversity and inclusion in education.")
scholarship7 = Scholarship("Global Leadership Scholarship", 7500, Donor("Donor7", "4444444444", "donor7@example.com"), 32000, 3.6, "International Relations", "2023-01-25", [], [], "For students displaying global leadership qualities.")
scholarship8 = Scholarship("Environmental Stewardship Award", 6000, Donor("Donor8", "5555555555", "donor8@example.com"), 30000, 3.3, "Environmental Science", "2022-11-05", [], [], "Recognizing commitment to environmental stewardship.")
scholarship9 = Scholarship("Entrepreneurship Excellence Scholarship", 6500, Donor("Donor9", "6666666666", "donor9@example.com"), 31000, 3.7, "Entrepreneurship", "2023-03-15", [], [], "Awarded for excellence in entrepreneurship.")
scholarship10 = Scholarship("Sports Achievement Grant", 5000, Donor("Donor10", "7777777777", "donor10@example.com"), 26000, 3.9, "Sports Science", "2022-10-15", [], [], "Recognizing outstanding sports achievements.")

tempData=[
    scholarship1,
    scholarship2,
    scholarship3,
    scholarship4,
    scholarship5,
    scholarship6,
    scholarship7,
    scholarship8,
    scholarship9,
    scholarship10
]