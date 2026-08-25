from app.database.database import SessionLocal

from app.models.course import Course
from app.models.skill import Skill
from app.models.skill_category import SkillCategory


# =========================================================
# COURSE CATALOGUE
# =========================================================

COURSES = [

    # =====================================================
    # IT & TECH SCIENCES
    # =====================================================

    {
        "title": "Python Programming Fundamentals",
        "description": "Learn Python programming from the basics, including variables, data types, conditions, loops and functions.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Python Programming",
    },

    {
        "title": "Advanced Python Development",
        "description": "Build advanced Python applications using object-oriented programming, modules, APIs and software architecture.",
        "level": "Advanced",
        "duration": "8 weeks",
        "skill": "Advanced Python",
    },

    {
        "title": "JavaScript Development",
        "description": "Learn modern JavaScript for building interactive web applications.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "JavaScript Development",
    },

    {
        "title": "Web Development Fundamentals",
        "description": "Learn how websites and web applications are designed, developed and deployed.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Web Development",
    },

    {
        "title": "Backend Development",
        "description": "Learn how to build APIs, backend services, authentication systems and database-connected applications.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Backend Development",
    },

    {
        "title": "Database Management",
        "description": "Learn database design, SQL queries, relationships and database management.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Database Management",
    },

    {
        "title": "Data Analysis",
        "description": "Learn how to collect, clean, analyse and visualize data to support decisions.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Data Analysis",
    },

    {
        "title": "Introduction to Artificial Intelligence",
        "description": "Understand artificial intelligence concepts and how intelligent software systems are built.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Artificial Intelligence",
    },

    {
        "title": "Machine Learning Fundamentals",
        "description": "Learn the foundations of machine learning, datasets, models, training and evaluation.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Machine Learning",
    },

    {
        "title": "Computer Vision with OpenCV",
        "description": "Learn image processing and computer vision techniques using OpenCV.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Computer Vision",
    },

    {
        "title": "Cybersecurity Fundamentals",
        "description": "Learn the fundamentals of protecting computers, networks, applications and information.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Cybersecurity",
    },

    {
        "title": "Cloud Computing Fundamentals",
        "description": "Learn the fundamentals of cloud infrastructure, deployment and cloud-based applications.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Cloud Computing",
    },


    # =====================================================
    # ENTREPRENEURSHIP & BUSINESS
    # =====================================================

    {
        "title": "Entrepreneurship Fundamentals",
        "description": "Learn how to identify opportunities, create business ideas and build sustainable businesses.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Entrepreneurship",
    },

    {
        "title": "Business Planning",
        "description": "Learn how to create practical business plans covering customers, operations, marketing and finances.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Business Planning",
    },

    {
        "title": "Product Development",
        "description": "Learn how to turn ideas into useful products that solve real customer problems.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Product Development",
    },

    {
        "title": "Sales Fundamentals",
        "description": "Learn customer discovery, communication, selling techniques and relationship building.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Sales",
    },

    {
        "title": "Customer Service",
        "description": "Develop professional customer service and communication skills.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Customer Service",
    },

    {
        "title": "Business Management",
        "description": "Learn how to manage people, resources, operations and business activities.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Business Management",
    },

    {
        "title": "Project Management",
        "description": "Learn how to plan, organize, execute and monitor projects successfully.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Project Management",
    },

    {
        "title": "Leadership Skills",
        "description": "Develop leadership, decision-making, teamwork and organizational skills.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Leadership",
    },

    {
        "title": "Financial Literacy",
        "description": "Learn budgeting, saving, revenue, expenses and basic financial decision-making.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Financial Literacy",
    },

    {
        "title": "Digital Business",
        "description": "Learn how to use digital technologies to create and grow modern businesses.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Digital Business",
    },


    # =====================================================
    # DIGITAL TECHNOLOGY
    # =====================================================

    {
        "title": "Digital Marketing Fundamentals",
        "description": "Learn how to promote products and services using digital marketing channels.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Digital Marketing",
    },

    {
        "title": "Social Media Management",
        "description": "Learn how to manage professional social media accounts and online communities.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Social Media Management",
    },

    {
        "title": "Graphic Design Fundamentals",
        "description": "Learn design principles, layouts, typography, branding and digital graphics.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Graphic Design",
    },

    {
        "title": "UI/UX Design",
        "description": "Learn how to design useful, accessible and engaging digital experiences.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "UI/UX Design",
    },

    {
        "title": "Content Creation",
        "description": "Learn how to create useful digital content for audiences and businesses.",
        "level": "Beginner",
        "duration": "5 weeks",
        "skill": "Content Creation",
    },

    {
        "title": "Search Engine Optimization",
        "description": "Learn the fundamentals of improving website visibility through search engines.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "SEO",
    },

    {
        "title": "WordPress Development",
        "description": "Learn how to build, customize and manage professional WordPress websites.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "WordPress Development",
    },

    {
        "title": "Digital Communication",
        "description": "Develop effective professional communication skills using digital platforms.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Digital Communication",
    },

    {
        "title": "Video Editing Fundamentals",
        "description": "Learn video editing, transitions, audio, effects and professional video production.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Video Editing",
    },

    {
        "title": "Computer Networking Fundamentals",
        "description": "Learn how computers and digital systems communicate across networks.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Computer Networking",
    },


    # =====================================================
    # MECHANICAL & CONSTRUCTION
    # =====================================================

    {
        "title": "Mechanical Maintenance",
        "description": "Learn maintenance procedures for mechanical equipment and machines.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Mechanical Maintenance",
    },

    {
        "title": "Welding Fundamentals",
        "description": "Learn the fundamentals of welding, equipment, materials and workshop safety.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Welding",
    },

    {
        "title": "Metal Fabrication",
        "description": "Learn how to design, cut, join and manufacture metal structures and components.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Fabrication",
    },

    {
        "title": "Plumbing Fundamentals",
        "description": "Learn installation and maintenance of domestic water and piping systems.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Plumbing",
    },

    {
        "title": "Carpentry Fundamentals",
        "description": "Learn woodworking, measurements, tools, joints and furniture construction.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Carpentry",
    },

    {
        "title": "Masonry Fundamentals",
        "description": "Learn basic block work, brickwork, construction techniques and site practices.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Masonry",
    },

    {
        "title": "Automotive Mechanics",
        "description": "Learn vehicle systems, diagnostics, maintenance and basic automotive repair.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Auto Mechanics",
    },

    {
        "title": "CNC Machining",
        "description": "Learn computer-controlled machining and modern manufacturing processes.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "CNC Machining",
    },

    {
        "title": "Technical Drawing",
        "description": "Learn accurate technical and engineering drawing techniques.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Technical Drawing",
    },

    {
        "title": "Construction Safety",
        "description": "Learn essential safety practices for construction and workshop environments.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Construction Safety",
    },


    # =====================================================
    # CREATIVE SKILLS & TECHNOLOGY
    # =====================================================

    {
        "title": "Architecture Fundamentals",
        "description": "Learn the fundamentals of building design, planning and architectural thinking.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Architecture",
    },

    {
        "title": "Furniture Design",
        "description": "Learn how to design functional and attractive furniture.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Furniture Design",
    },

    {
        "title": "Interior Design",
        "description": "Learn how to design functional and attractive interior environments.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Interior Design",
    },

    {
        "title": "3D Modeling Fundamentals",
        "description": "Learn the fundamentals of creating and editing three-dimensional digital models.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "3D Modeling",
    },

    {
        "title": "3D Printing",
        "description": "Learn how digital 3D models are prepared and converted into physical objects.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "3D Printing",
    },

    {
        "title": "Photography Fundamentals",
        "description": "Learn composition, lighting, camera settings and professional photography techniques.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Photography",
    },

    {
        "title": "Animation Fundamentals",
        "description": "Learn the principles and techniques used to create animated digital content.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Animation",
    },

    {
        "title": "Creative Problem Solving",
        "description": "Learn structured techniques for developing creative solutions to practical problems.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Creative Problem Solving",
    },


    # =====================================================
    # ELECTRONICS TECHNOLOGY
    # =====================================================

    {
        "title": "Electronics Repair Fundamentals",
        "description": "Learn how to diagnose and repair common electronic devices.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Electronics Repair",
    },

    {
        "title": "Digital Electronics",
        "description": "Learn digital logic, circuits and basic digital electronic systems.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Digital Electronics",
    },

    {
        "title": "Analog Electronics",
        "description": "Learn the principles of analog circuits and electronic components.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Analog Electronics",
    },

    {
        "title": "Arduino Electronics Projects",
        "description": "Learn how to build programmable electronics projects using Arduino.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Arduino",
    },

    {
        "title": "Raspberry Pi Projects",
        "description": "Learn how to use Raspberry Pi computers for automation and practical projects.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Raspberry Pi",
    },

    {
        "title": "Embedded Systems Fundamentals",
        "description": "Learn the fundamentals of developing software and hardware for embedded devices.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Embedded Systems",
    },

    {
        "title": "Robotics Fundamentals",
        "description": "Learn the fundamentals of robotic systems, sensors, actuators and programming.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Robotics",
    },

    {
        "title": "Drone Technology Fundamentals",
        "description": "Learn the fundamentals of drone systems, components, control and applications.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Drone Technology",
    },

    {
        "title": "PCB Design Fundamentals",
        "description": "Learn how to design printed circuit boards for electronic systems.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "PCB Design",
    },

    {
        "title": "Sensors & Instrumentation",
        "description": "Learn how sensors measure physical quantities and how instrumentation systems work.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Sensors & Instrumentation",
    },


    # =====================================================
    # ELECTRICAL & ENERGY
    # =====================================================

    {
        "title": "Electrical Installation",
        "description": "Learn the fundamentals of safe electrical installation and wiring.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Electrical Installation",
    },

    {
        "title": "Electrical Maintenance",
        "description": "Learn how to troubleshoot and maintain electrical systems.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Electrical Maintenance",
    },

    {
        "title": "Solar Energy Systems",
        "description": "Learn how solar power systems are designed, installed and maintained.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Solar Energy",
    },

    {
        "title": "Renewable Energy Fundamentals",
        "description": "Explore renewable energy technologies and their practical applications.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Renewable Energy",
    },

    {
        "title": "Generator Maintenance",
        "description": "Learn how to maintain and troubleshoot electrical generators.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Generator Maintenance",
    },

    {
        "title": "Electric Motor Control",
        "description": "Learn the principles of electric motor control and maintenance.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Motor Control",
    },

    {
        "title": "Electrical Power Systems",
        "description": "Learn the fundamentals of electrical power generation, transmission and distribution.",
        "level": "Advanced",
        "duration": "10 weeks",
        "skill": "Power Systems",
    },

    {
        "title": "Smart Home Systems",
        "description": "Learn how intelligent home systems are installed and integrated.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Smart Home Systems",
    },

    {
        "title": "Electrical Safety",
        "description": "Learn essential electrical safety procedures and practices.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Electrical Safety",
    },


    # =====================================================
    # BEAUTY & PERSONAL CARE
    # =====================================================

    {
        "title": "Professional Hair Styling",
        "description": "Learn professional hair styling techniques and grooming practices.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Hair Styling",
    },

    {
        "title": "Hair Braiding",
        "description": "Learn professional braiding techniques and popular styles.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Hair Braiding",
    },

    {
        "title": "Makeup Artistry",
        "description": "Learn professional makeup application techniques.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Makeup Artistry",
    },

    {
        "title": "Skincare Fundamentals",
        "description": "Learn basic skincare practices and personal care routines.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Skincare",
    },

    {
        "title": "Professional Nail Care",
        "description": "Learn professional nail care, maintenance and styling.",
        "level": "Beginner",
        "duration": "5 weeks",
        "skill": "Nail Care",
    },

    {
        "title": "Professional Barbering",
        "description": "Learn professional haircutting and grooming techniques.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Barbering",
    },

    {
        "title": "Beauty Business",
        "description": "Learn how to manage and grow a beauty service business.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Beauty Business",
    },


    # =====================================================
    # HOME & APPLIANCE REPAIRS
    # =====================================================

    {
        "title": "Home Appliance Repair",
        "description": "Learn how to diagnose and repair common household appliances.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Home Appliance Repair",
    },

    {
        "title": "Refrigerator Repair",
        "description": "Learn the fundamentals of refrigeration systems and refrigerator maintenance.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Refrigerator Repair",
    },

    {
        "title": "Washing Machine Repair",
        "description": "Learn how to diagnose and repair washing machines.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Washing Machine Repair",
    },

    {
        "title": "Air Conditioner Repair",
        "description": "Learn the fundamentals of air conditioning maintenance and repair.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Air Conditioner Repair",
    },

    {
        "title": "Television Repair",
        "description": "Learn how to diagnose and repair television systems.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Television Repair",
    },

    {
        "title": "Water Pump Repair",
        "description": "Learn how to maintain and repair domestic water pumps.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Water Pump Repair",
    },

    {
        "title": "Furniture Repair",
        "description": "Learn techniques for repairing and restoring household furniture.",
        "level": "Beginner",
        "duration": "5 weeks",
        "skill": "Furniture Repair",
    },


    # =====================================================
    # FASHION
    # =====================================================

    {
        "title": "Fashion Design Fundamentals",
        "description": "Learn the fundamentals of designing clothing and fashion products.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Fashion Design",
    },

    {
        "title": "Professional Tailoring",
        "description": "Learn garment construction, measurements and clothing alteration.",
        "level": "Beginner",
        "duration": "10 weeks",
        "skill": "Tailoring",
    },

    {
        "title": "Pattern Making",
        "description": "Learn how to create accurate patterns for garment production.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Pattern Making",
    },

    {
        "title": "Leatherwork",
        "description": "Learn how to create useful products from leather materials.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Leatherwork",
    },

    {
        "title": "Shoemaking",
        "description": "Learn the fundamentals of designing and manufacturing footwear.",
        "level": "Intermediate",
        "duration": "10 weeks",
        "skill": "Shoemaking",
    },

    {
        "title": "Bag Making",
        "description": "Learn how to design and manufacture bags and accessories.",
        "level": "Beginner",
        "duration": "6 weeks",
        "skill": "Bag Making",
    },

    {
        "title": "Fashion Business",
        "description": "Learn how to manage and grow a fashion business.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Fashion Business",
    },

    {
        "title": "Textile Production",
        "description": "Learn the fundamentals of textile materials and production.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Textile Production",
    },


    # =====================================================
    # FOOD & HOSPITALITY
    # =====================================================

    {
        "title": "Professional Cooking",
        "description": "Learn cooking techniques, kitchen practices and meal preparation.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Cooking",
    },

    {
        "title": "Baking Fundamentals",
        "description": "Learn how to prepare bread, cakes and other baked products.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Baking",
    },

    {
        "title": "Catering",
        "description": "Learn how to provide professional food services for events and organizations.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Catering",
    },

    {
        "title": "Food Preservation",
        "description": "Learn safe techniques for preserving food for longer storage.",
        "level": "Beginner",
        "duration": "5 weeks",
        "skill": "Food Preservation",
    },

    {
        "title": "Food Safety",
        "description": "Learn safe food handling, hygiene and food safety practices.",
        "level": "Beginner",
        "duration": "4 weeks",
        "skill": "Food Safety",
    },

    {
        "title": "Hospitality Management",
        "description": "Learn how to manage hospitality operations and customer experience.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Hospitality Management",
    },

    {
        "title": "Restaurant Management",
        "description": "Learn how to manage restaurant operations, staff and customer service.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Restaurant Management",
    },

    {
        "title": "Pastry Making",
        "description": "Learn professional pastry preparation techniques.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Pastry Making",
    },


    # =====================================================
    # AGRICULTURE & ANIMAL SKILLS
    # =====================================================

    {
        "title": "Crop Farming Fundamentals",
        "description": "Learn how to plan and manage crop production.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Crop Farming",
    },

    {
        "title": "Livestock Farming",
        "description": "Learn the fundamentals of managing and raising farm animals.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Livestock Farming",
    },

    {
        "title": "Poultry Farming",
        "description": "Learn how to manage poultry production systems.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Poultry Farming",
    },

    {
        "title": "Fish Farming",
        "description": "Learn the fundamentals of aquaculture and fish production.",
        "level": "Beginner",
        "duration": "8 weeks",
        "skill": "Fish Farming",
    },

    {
        "title": "Agricultural Irrigation",
        "description": "Learn how irrigation systems support agricultural production.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Irrigation",
    },

    {
        "title": "Agricultural Technology",
        "description": "Learn how modern technology can improve agricultural production.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Agricultural Technology",
    },

    {
        "title": "Food Processing",
        "description": "Learn how agricultural products can be processed into useful food products.",
        "level": "Intermediate",
        "duration": "8 weeks",
        "skill": "Food Processing",
    },

    {
        "title": "Farm Business Management",
        "description": "Learn how to manage agricultural businesses, resources and finances.",
        "level": "Intermediate",
        "duration": "6 weeks",
        "skill": "Farm Business Management",
    },
]


# =========================================================
# SEED COURSES
# =========================================================

def seed_courses():

    db = SessionLocal()

    try:

        created = 0
        existing = 0
        missing_skills = 0

        print("=" * 40)
        print("       EarnFix Course Seeder")
        print("=" * 40)

        for item in COURSES:

            skill = (
                db.query(Skill)
                .filter(
                    Skill.name == item["skill"]
                )
                .first()
            )

            if not skill:

                print(
                    f"WARNING: Skill not found: {item['skill']}"
                )

                missing_skills += 1
                continue

            category = (
                db.query(SkillCategory)
                .filter(
                    SkillCategory.id == skill.category_id
                )
                .first()
            )

            if not category:

                print(
                    f"WARNING: Category not found for skill: {item['skill']}"
                )

                missing_skills += 1
                continue

            existing_course = (
                db.query(Course)
                .filter(
                    Course.title == item["title"]
                )
                .first()
            )

            if existing_course:

                existing += 1
                continue

            course = Course(
                title=item["title"],
                description=item["description"],
                level=item["level"],
                duration=item["duration"],
                category_id=category.id,
                skill_id=skill.id,
            )

            db.add(course)
            created += 1

        db.commit()

        total_courses = db.query(Course).count()

        print()
        print(f"Courses created: {created}")
        print(f"Courses already existed: {existing}")
        print(f"Missing skills/categories: {missing_skills}")
        print(f"Total courses: {total_courses}")
        print("=" * 40)

    except Exception as error:

        db.rollback()

        print()
        print("ERROR SEEDING COURSES")
        print(error)

        raise

    finally:

        db.close()


if __name__ == "__main__":
    seed_courses()