import sqlite3
from pathlib import Path

DATABASE = Path(__file__).with_name("ncerc.db")


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            keywords TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    existing = connection.execute(
        "SELECT COUNT(*) FROM knowledge"
    ).fetchone()[0]

    if existing == 0:
        knowledge = [

            (
                "greeting",
                "hi,hello,hey,good morning,good afternoon,good evening",
                "Hello! 👋 I'm the NCERC College Assistant. How can I help you with admissions, courses, academics, library, campus life or other college information?"
            ),
            (
    "attendance",
    "attendance minimum attendance",
    "Students must maintain the attendance percentage specified by the university regulations."
),

(
    "lab",
    "lab,laboratory",
    "NCERC provides modern laboratories for practical learning in various departments."
),

(
    "project",
    "project,final year project",
    "Students are required to complete project work as part of their academic curriculum."
),

(
    "faculty",
    "faculty,teachers,staff",
    "NCERC has experienced faculty members across all departments."
),

(
    "academic_calendar",
    "academic calendar,college calendar",
    "The academic calendar is available on the college website."
),

(
    "ktu",
    "ktu,university",
    "NCERC is affiliated with APJ Abdul Kalam Technological University (KTU)."
),

(
    "autonomous",
    "autonomous status,is ncerc autonomous",
    "Yes, NCERC is an autonomous institution."
),

(
    "nss",
    "nss",
    "The National Service Scheme (NSS) unit conducts social service and community activities."
),(
    "uniform",
    "uniform,dress code",
    "Students are expected to follow the dress code prescribed by the college."
),

(
    "leave",
    "leave application,leave request",
    "Leave applications should be submitted to the class advisor or department office."
),

(
    "attendance_shortage",
    "attendance shortage,low attendance",
    "Students with attendance shortage may need to submit a valid explanation and follow university regulations."
),

(
    "student_portal",
    "student portal,portal login",
    "The student portal can be accessed using your registered credentials."
),

(
    "certificate_courses",
    "certificate course,add on course",
    "NCERC offers various value-added and certificate courses to improve student skills."
),

(
    "research",
    "research,research activities",
    "Students and faculty actively participate in research and innovation activities."
),

(
    "innovation",
    "innovation,startup,entrepreneurship",
    "The college encourages innovation, startups and entrepreneurship through various programs."
),

(
    "industry_visit",
    "industrial visit,industry visit",
    "Departments regularly organize industrial visits to provide practical exposure."
),

(
    "mentor",
    "mentor,faculty advisor",
    "Each student is assigned a faculty advisor for academic guidance."
),

(
    "anti_ragging",
    "anti ragging,ragging complaint",
    "NCERC follows a strict anti-ragging policy and maintains an Anti-Ragging Committee."
),

(
    "lost_found",
    "lost item,lost and found",
    "Please contact the administration office regarding lost and found items."
),

(
    "bank",
    "atm,bank facility",
    "Students can use nearby banking and ATM facilities available around the campus."
),

(
    "electricity",
    "power backup,generator",
    "Backup power facilities are available for essential campus operations."
),

(
    "holidays",
    "holidays,vacation",
    "Holiday schedules are announced through the academic calendar and official notifications."
),

(
    "od",
    "od,on duty",
    "On-Duty requests must be approved by the concerned faculty and department."
),

(
    "workshop_registration",
    "register workshop,workshop registration",
    "Workshop registration details are announced through department notices and event coordinators."
),

(
    "seminar",
    "seminar,presentation",
    "Seminars are conducted regularly to improve communication and technical skills."
),

(
    "project_guidance",
    "project guide,project supervisor",
    "Project supervisors are assigned by the department based on the project area."
),

(
    "higher_studies",
    "higher studies,gate,cat,gre",
    "Students receive guidance for higher studies and competitive examinations."
),

(
    "alumni",
    "alumni,old students",
    "The college maintains an alumni network to support students and graduates."
),

(
    "campus_interview",
    "campus interview,interview preparation",
    "Placement training sessions are conducted to prepare students for campus interviews."
),

(
    "coding",
    "coding club,programming club",
    "Technical clubs and coding activities are organized for interested students."
),

(
    "hackathon",
    "hackathon,coding competition",
    "Students are encouraged to participate in hackathons and technical competitions."
),

(
    "language_lab",
    "language lab,communication lab",
    "Language and communication skill development facilities are available."
),

(
    "career_guidance",
    "career guidance,career counseling",
    "Career guidance programs help students plan their professional future."
),

(
    "student_support",
    "student support,help desk",
    "Student support services are available for academic and administrative assistance."
),

(
    "environment",
    "green campus,environment",
    "NCERC promotes environmental awareness through various green initiatives."
),

(
    "cultural_fest",
    "cultural fest,cultural programs",
    "The college organizes cultural events and celebrations throughout the year."
),

(
    "technical_fest",
    "technical fest,tech fest",
    "Technical festivals provide opportunities for students to showcase innovation and skills."
),

(
    "discipline",
    "discipline,rules",
    "Students are expected to follow college rules and maintain discipline on campus."
),

(
    "ncc",
    "ncc",
    "Students can join NCC activities through the college NCC unit."
),

(
    "events",
    "events,fest,programs",
    "NCERC regularly organizes technical fests, cultural programs, workshops and seminars."
),

(
    "workshop",
    "workshop,seminar",
    "Workshops and seminars are conducted regularly to improve technical and professional skills."
),

(
    "campus",
    "campus,campus life",
    "NCERC offers a vibrant campus life with clubs, sports, cultural activities and technical events."
),

(
    "parking",
    "parking,vehicle parking",
    "Parking facilities are available for students, faculty and visitors."
),

(
    "ragging",
    "ragging,anti ragging",
    "NCERC follows a strict anti-ragging policy to ensure a safe campus environment."
),

(
    "emergency",
    "emergency,medical emergency",
    "Please contact the administration office or nearest faculty member immediately in case of emergencies."
),
(
    "who_are_you",
    "who are you,what are you,about yourself",
    "I am the NCERC College Assistant chatbot. I can help you with admissions, courses, library, hostel, exams, placements and other college-related information."
),

(
    "how_are_you",
    "how are you,how are you doing",
    "I'm doing great! 😊 Thank you for asking. How can I help you today?"
),

(
    "creator",
    "who made you,who created you,developer",
    "I was developed as a college assistance project to help students find information quickly."
),

(
    "purpose",
    "why are you here,what is your purpose",
    "My purpose is to help students and visitors get information about NCERC easily."
),

(
    "your_name",
    "what is your name,who am i talking to",
    "My name is NCERC College Assistant."
),

(
    "joke",
    "tell me a joke,joke,make me laugh",
    "Why did the student bring a ladder to college? Because they wanted to go to the next level! 😄"
),

(
    "motivation",
    "motivate me,motivation,inspiration",
    "Success is the sum of small efforts repeated every day. Keep learning and keep growing! 🚀"
),

(
    "ai",
    "are you ai,artificial intelligence",
    "I am a simple college assistant chatbot designed to answer questions about NCERC."
),

(
    "help",
    "help,what can you do",
    "I can answer questions about admissions, courses, fees, hostel, library, placements, exams and campus facilities."
),

(
    "time",
    "what time is it,current time",
    "Please check your device clock for the current time."
),
              ("college_name",
"name,college name,college",
"The name of the college is NCERC College of Engineering."),

("location",
"location,where is the college,college location,address",
"The college is located in Nila Gardens, Pampady, Thrissur, Kerala."),

("timings",
"college timings,working hours,college hours",
"College working hours are 9:00 AM to 4:30 PM from Monday to Friday."),

("contact",
"contact,phone,email,contact college",
"You can contact us by phone, email, or by visiting the administration office."),

("courses",
"courses,programs,what courses are offered,btech,mtech,mba",
"We offer B.Tech, M.Tech, MBA, MCA and other programs."),

("admission",
"admission,apply admission,how to apply",
"Admissions can be completed online through the college website or at the admission office."),

("documents",
"documents required,admission documents,certificates",
"Mark sheets, Transfer Certificate, Aadhaar Card, Passport-size photos and other required certificates are needed."),

("admission_fee",
"admission fee,fee for admission",
"The admission fee varies depending on the course selected."),

("hostel",
"hostel,hostel facility,boys hostel,girls hostel",
"Yes, separate hostel facilities are available for boys and girls."),

("transport",
"bus,transport,college bus",
"Yes, bus transportation is available on selected routes."),

("library_location",
"library,where is library,library location",
"The library is located on the first floor of Block A."),

("library_timings",
"library timings,library hours",
"The library is open from 8:30 AM to 5:30 PM."),

("library_books",
"borrow books,library books",
"Students can borrow up to three books at a time."),

("hostel_fee",
"hostel fee,hostel fees",
"Hostel fees vary according to room type and facilities."),

("fee_payment",
"pay fees,college fees,payment",
"Fees can be paid online or at the college accounts office."),

("fee_deadline",
"last date fee payment,fee deadline",
"The last date is announced every semester through official notifications."),

("semester_exam",
"semester exam,exam date",
"Semester exams are conducted according to the academic calendar."),

("hall_ticket",
"hall ticket,download hall ticket",
"Hall tickets can be downloaded from the student portal."),

("results",
"exam result,results",
"Results are usually published within one month after the exams."),

("revaluation",
"revaluation,apply revaluation",
"Apply through the examination cell before the deadline."),

("principal",
"principal,who is principal",
"Please refer to the college website for the latest Principal details."),

("hod_cse",
"hod cse,head of cse,cse hod",
"Please visit the CSE department office or website for updated information."),

("departments",
"departments,branches",
"CSE, ECE, EEE, Mechanical, Civil, MBA, MCA and others are available."),

("semesters",
"semesters,total semesters",
"Most undergraduate courses have eight semesters."),

("syllabus",
"syllabus,course syllabus",
"The syllabus is available on the college website and department office."),

("wifi",
"wifi,internet",
"Yes, campus-wide Wi-Fi is available for students and staff."),

("computer_lab",
"computer lab,lab",
"The computer lab is located in the CSE Block."),

("sports",
"sports,games,playground",
"Cricket, football, volleyball, basketball, badminton and indoor games are available."),

("canteen",
"canteen,food",
"Yes, the college has a hygienic canteen."),

("canteen_timings",
"canteen timings,canteen hours",
"The canteen is open from 8:00 AM to 5:00 PM."),

("id_card",
"id card,student id",
"Apply through the student affairs office after admission."),

("bonafide",
"bonafide certificate",
"Submit an application to the administration office."),

("tc",
"transfer certificate,tc",
"Apply at the office after completing all formalities."),

("scholarship",
"scholarship,scholarships",
"Yes, government and merit scholarships are available."),

("scholarship_apply",
"apply scholarship,scholarship application",
"Apply through the scholarship portal or the college office."),

("internship",
"internship,internships",
"Yes, internship opportunities are provided through the placement cell."),

("placement",
"placement,placements,job",
"Yes, the placement cell conducts recruitment drives and training."),

("companies",
"placement companies,recruiters",
"Many IT, Core Engineering and Business companies visit every year."),

("placement_officer",
"placement officer",
"Please check the placement office notice board or website."),

("training",
"training programs,training",
"Technical and soft skill training programs are organized regularly."),

("clubs",
"student clubs,clubs",
"Technical, Cultural, Sports, NSS, NCC and Innovation Clubs are available."),

("join_club",
"join club,register club",
"Contact the faculty coordinator of the respective club."),

("events",
"college events,register event",
"Register through the event coordinator or online portal."),

("notices",
"notices,notice board",
"Notices are displayed on the notice board and college website."),

("complaint",
"complaint,grievance",
"Submit your complaint to the grievance cell or online portal."),

("medical",
"medical assistance,first aid",
"Yes, first aid and emergency medical support are available."),

("office_hours",
"office hours,administration hours",
"The administration office works from 9:00 AM to 4:30 PM."),

("admin_contact",
"administration office contact",
"Visit the office or contact through the official phone number or email."),

         ("parents",
         "parents meet faculty,parent meeting",
               "Yes, during working hours with prior appointment."),

        ("thanks",
            "thank you,thanks",
             "You're welcome! Have a great day. Feel free to ask if you need any more information."),

         (
                "college",
                "about ncerc,college,nehru college,about college",
                "Nehru College of Engineering & Research Centre (NCERC) is an autonomous engineering institution in Kerala affiliated with APJ Abdul Kalam Technological University (KTU)."
            ),

         (
                "courses",
                "courses,course,programs,programmes,branches,degree,what can i study",
                "NCERC offers undergraduate and postgraduate programs including B.Tech, M.Tech, MBA and MCA. The current college website lists engineering and emerging disciplines such as Computer Science & Engineering, Artificial Intelligence & Data Science, Mechanical Engineering, Electrical & Electronics Engineering, Mechatronics and others."
            ),

            (
                "library",
                "library,books,reading room,digital library,library timing",
                "The NCERC central library provides books, journals and digital learning resources. An official NCERC self-study report states that the library was open from 8:00 AM to 8:00 PM except Sundays and government holidays. Please verify current timings with the college before relying on them."
            ),

            (
                "location",
                "location,address,where is college,where is ncerc,place",
                "NCERC is located at Pampady, Thiruvilwamala, Thrissur, Kerala."
            ),

            (
                "admission",
                "admission,admissions,apply,application,join,college admission",
                "For current admission information, eligibility, application procedures and available seats, please check the official NCERC admissions information because admission requirements can change between academic years."
            ),

            (
                "placement",
                "placement,placements,jobs,recruitment,companies,career",
                "NCERC has a placement and career-support system for students. For current placement statistics, recruiters and package information, the latest official placement information should be checked because these figures change by academic year."
            ),

            (
                "autonomous",
                "autonomous,ugc status,autonomous status",
                "NCERC has autonomous status granted by UGC. Its autonomous status provides academic flexibility in curriculum and evaluation."
            ),

            (
                "contact",
                "contact,phone,email,helpline,office",
                "For current contact details, please use the official NCERC website's Contact section so that you receive the latest phone numbers and email addresses."
            ),

            (
                "thank",
                "thanks,thank you,thank,thankyou",
                "You're welcome! 😊 I'm always happy to help with NCERC-related questions."
            ),
            (
    "uniform",
    "uniform,dress code",
    "Students are expected to follow the dress code prescribed by the college."
),

(
    "leave",
    "leave application,leave request",
    "Leave applications should be submitted to the class advisor or department office."
),

(
    "attendance_shortage",
    "attendance shortage,low attendance",
    "Students with attendance shortage may need to submit a valid explanation and follow university regulations."
),

(
    "student_portal",
    "student portal,portal login",
    "The student portal can be accessed using your registered credentials."
),

(
    "certificate_courses",
    "certificate course,add on course",
    "NCERC offers various value-added and certificate courses to improve student skills."
),

(
    "research",
    "research,research activities",
    "Students and faculty actively participate in research and innovation activities."
),

(
    "innovation",
    "innovation,startup,entrepreneurship",
    "The college encourages innovation, startups and entrepreneurship through various programs."
),

(
    "industry_visit",
    "industrial visit,industry visit",
    "Departments regularly organize industrial visits to provide practical exposure."
),

(
    "mentor",
    "mentor,faculty advisor",
    "Each student is assigned a faculty advisor for academic guidance."
),

(
    "anti_ragging",
    "anti ragging,ragging complaint",
    "NCERC follows a strict anti-ragging policy and maintains an Anti-Ragging Committee."
),

(
    "lost_found",
    "lost item,lost and found",
    "Please contact the administration office regarding lost and found items."
),

(
    "bank",
    "atm,bank facility",
    "Students can use nearby banking and ATM facilities available around the campus."
),

(
    "electricity",
    "power backup,generator",
    "Backup power facilities are available for essential campus operations."
),

(
    "holidays",
    "holidays,vacation",
    "Holiday schedules are announced through the academic calendar and official notifications."
),

(
    "od",
    "od,on duty",
    "On-Duty requests must be approved by the concerned faculty and department."
),

(
    "workshop_registration",
    "register workshop,workshop registration",
    "Workshop registration details are announced through department notices and event coordinators."
),

(
    "seminar",
    "seminar,presentation",
    "Seminars are conducted regularly to improve communication and technical skills."
),

(
    "project_guidance",
    "project guide,project supervisor",
    "Project supervisors are assigned by the department based on the project area."
),

(
    "higher_studies",
    "higher studies,gate,cat,gre",
    "Students receive guidance for higher studies and competitive examinations."
),

(
    "alumni",
    "alumni,old students",
    "The college maintains an alumni network to support students and graduates."
),

(
    "campus_interview",
    "campus interview,interview preparation",
    "Placement training sessions are conducted to prepare students for campus interviews."
),

(
    "coding",
    "coding club,programming club",
    "Technical clubs and coding activities are organized for interested students."
),

(
    "hackathon",
    "hackathon,coding competition",
    "Students are encouraged to participate in hackathons and technical competitions."
),

(
    "language_lab",
    "language lab,communication lab",
    "Language and communication skill development facilities are available."
),

(
    "career_guidance",
    "career guidance,career counseling",
    "Career guidance programs help students plan their professional future."
),

(
    "student_support",
    "student support,help desk",
    "Student support services are available for academic and administrative assistance."
),

(
    "environment",
    "green campus,environment",
    "NCERC promotes environmental awareness through various green initiatives."
),

(
    "cultural_fest",
    "cultural fest,cultural programs",
    "The college organizes cultural events and celebrations throughout the year."
),

(
    "technical_fest",
    "technical fest,tech fest",
    "Technical festivals provide opportunities for students to showcase innovation and skills."
),

(
    "discipline",
    "discipline,rules",
    "Students are expected to follow college rules and maintain discipline on campus."
),(
    "parking",
    "parking,vehicle parking,bike parking,car parking",
    "Parking facilities are available inside the campus for students and staff."
),

(
    "mobile",
    "mobile phone,phone usage,use phone in class",
    "Students should follow classroom rules regarding mobile phone usage."
),

(
    "lost_id",
    "lost id card,id card lost",
    "Please report the loss to the Student Affairs Office and apply for a replacement ID card."
),

(
    "certificate",
    "course completion certificate,certificate",
    "Certificates can be collected from the concerned department or office after processing."
),

(
    "elective",
    "elective subject,open elective",
    "Elective subjects are offered according to the curriculum and department guidelines."
),

(
    "lab_exam",
    "lab exam,practical exam",
    "Practical examinations are conducted according to the academic schedule."
),

(
    "mentor",
    "mentor,faculty advisor,class advisor",
    "Students can contact their faculty advisor for academic guidance and support."
),

(
    "first_year",
    "first year,first year students",
    "First-year students have dedicated faculty support and orientation programs."
),

(
    "orientation",
    "orientation,induction program",
    "Orientation programs are conducted to help new students adapt to college life."
),

(
    "guest_lecture",
    "guest lecture,expert talk",
    "Guest lectures are organized regularly with industry experts and academicians."
),

(
    "industrial_visit",
    "industrial visit,industry visit",
    "Departments organize industrial visits to provide practical industry exposure."
),

(
    "innovation",
    "innovation,startup,entrepreneurship",
    "The college encourages innovation and entrepreneurship through various activities."
),

(
    "competition",
    "competition,contest,event competition",
    "Students are encouraged to participate in technical, cultural and sports competitions."
),

(
    "campus_safety",
    "safety,security,campus security",
    "Campus security measures are in place to ensure student safety."
),

(
    "emergency_contact",
    "emergency,emergency contact",
    "For emergencies, immediately contact the administration office or nearest faculty member."
)
        ]

        connection.executemany(
            """
            INSERT INTO knowledge (category, keywords, answer)
            VALUES (?, ?, ?)
            """,
            knowledge
        )

    connection.commit()
    connection.close()


def get_all_knowledge():
    connection = get_connection()

    rows = connection.execute(
        "SELECT * FROM knowledge"
    ).fetchall()

    connection.close()

    return rows