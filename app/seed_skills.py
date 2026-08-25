from app.database.database import SessionLocal

# Load all models so SQLAlchemy relationships are registered.
from app.models.user import User
from app.models.profile import StudentProfile
from app.models.skill_category import SkillCategory
from app.models.skill import Skill


SKILLS = {
    "IT & Tech Sciences": [
        ("Python Programming", "Programming with Python for automation, software and AI.", "Beginner"),
        ("Advanced Python", "Advanced Python programming, architecture and software development.", "Advanced"),
        ("JavaScript Development", "Modern JavaScript programming for web applications.", "Intermediate"),
        ("Web Development", "Building modern websites and web applications.", "Beginner"),
        ("Backend Development", "Building APIs, services and backend systems.", "Intermediate"),
        ("Database Management", "Designing, querying and maintaining databases.", "Intermediate"),
        ("Data Analysis", "Using data to discover insights and support decisions.", "Intermediate"),
        ("Artificial Intelligence", "Building and using intelligent software systems.", "Intermediate"),
        ("Machine Learning", "Developing machine learning models and applications.", "Intermediate"),
        ("Computer Vision", "Computer vision and image processing systems.", "Intermediate"),
        ("Cybersecurity", "Protecting systems, networks and information from threats.", "Intermediate"),
        ("Cloud Computing", "Deploying and managing applications using cloud platforms.", "Intermediate"),
    ],

    "Entrepreneurship & Business Development": [
        ("Entrepreneurship", "Starting, developing and managing a business.", "Beginner"),
        ("Business Planning", "Creating structured plans for business development.", "Beginner"),
        ("Product Development", "Designing and developing products for customers.", "Intermediate"),
        ("Sales", "Selling products and services effectively.", "Beginner"),
        ("Customer Service", "Building strong customer relationships and support.", "Beginner"),
        ("Business Management", "Managing people, resources and business operations.", "Intermediate"),
        ("Project Management", "Planning and delivering projects successfully.", "Intermediate"),
        ("Leadership", "Leading teams and making effective organizational decisions.", "Intermediate"),
        ("Financial Literacy", "Understanding budgets, revenue, expenses and financial decisions.", "Beginner"),
        ("Digital Business", "Using digital technologies to operate and grow businesses.", "Intermediate"),
    ],

    "Digital Technology": [
        ("Digital Marketing", "Promoting products and services through digital channels.", "Beginner"),
        ("Social Media Management", "Managing professional social media accounts and communities.", "Beginner"),
        ("Graphic Design", "Creating visual designs for digital and print communication.", "Beginner"),
        ("UI/UX Design", "Designing useful, accessible and engaging digital experiences.", "Intermediate"),
        ("Content Creation", "Creating useful digital content for audiences and businesses.", "Beginner"),
        ("SEO", "Improving online visibility through search engine optimization.", "Intermediate"),
        ("WordPress Development", "Building and managing websites with WordPress.", "Beginner"),
        ("Digital Communication", "Using digital platforms for effective professional communication.", "Beginner"),
        ("Video Editing", "Editing and producing professional video content.", "Intermediate"),
        ("Computer Networking", "Connecting and managing computers and digital systems.", "Intermediate"),
    ],

    "Mechanical & Construction Technology": [
        ("Mechanical Maintenance", "Maintaining and servicing mechanical equipment.", "Intermediate"),
        ("Welding", "Joining metals using welding techniques.", "Beginner"),
        ("Fabrication", "Designing and manufacturing metal structures and components.", "Intermediate"),
        ("Plumbing", "Installing and maintaining water and piping systems.", "Beginner"),
        ("Carpentry", "Constructing and repairing wooden structures and furniture.", "Beginner"),
        ("Masonry", "Constructing structures using blocks, bricks and related materials.", "Beginner"),
        ("Auto Mechanics", "Diagnosing and repairing motor vehicles.", "Intermediate"),
        ("CNC Machining", "Computer-controlled machining and manufacturing.", "Intermediate"),
        ("Technical Drawing", "Creating accurate technical engineering drawings.", "Beginner"),
        ("Construction Safety", "Applying safety practices in construction environments.", "Beginner"),
    ],

    "Creative Skills & Technology": [
        ("Architecture", "Planning and designing buildings and physical spaces.", "Intermediate"),
        ("Furniture Design", "Designing functional and attractive furniture.", "Intermediate"),
        ("Interior Design", "Designing functional and attractive interior environments.", "Intermediate"),
        ("3D Modeling", "Creating three-dimensional digital models.", "Intermediate"),
        ("3D Printing", "Producing physical objects from digital 3D models.", "Intermediate"),
        ("Photography", "Capturing professional photographs for communication and business.", "Beginner"),
        ("Animation", "Creating animated digital content.", "Intermediate"),
        ("Creative Problem Solving", "Developing creative solutions to practical problems.", "Beginner"),
    ],

    "Electronics Technology": [
        ("Electronics Repair", "Diagnosing and repairing electronic devices.", "Beginner"),
        ("Digital Electronics", "Understanding and designing digital electronic circuits.", "Intermediate"),
        ("Analog Electronics", "Understanding and working with analog circuits.", "Intermediate"),
        ("Arduino", "Building programmable electronics projects using Arduino.", "Beginner"),
        ("Raspberry Pi", "Using Raspberry Pi computers for projects and automation.", "Beginner"),
        ("Embedded Systems", "Developing software and hardware for embedded devices.", "Intermediate"),
        ("Robotics", "Designing and programming robotic systems.", "Intermediate"),
        ("Drone Technology", "Understanding drone systems and their applications.", "Intermediate"),
        ("PCB Design", "Designing printed circuit boards for electronic systems.", "Intermediate"),
        ("Sensors & Instrumentation", "Using sensors to measure and monitor physical systems.", "Intermediate"),
    ],

    "Electrical & Energy": [
        ("Electrical Installation", "Installing electrical systems safely and correctly.", "Beginner"),
        ("Electrical Maintenance", "Maintaining and troubleshooting electrical systems.", "Intermediate"),
        ("Solar Energy", "Designing and maintaining solar power systems.", "Intermediate"),
        ("Renewable Energy", "Understanding renewable energy technologies and systems.", "Intermediate"),
        ("Generator Maintenance", "Maintaining and troubleshooting electrical generators.", "Intermediate"),
        ("Motor Control", "Controlling and maintaining electric motors.", "Intermediate"),
        ("Power Systems", "Understanding electrical power generation and distribution.", "Advanced"),
        ("Smart Home Systems", "Installing and integrating intelligent home systems.", "Intermediate"),
        ("Electrical Safety", "Applying electrical safety procedures and practices.", "Beginner"),
    ],

    "Beauty & Personal Care": [
        ("Hair Styling", "Professional hair styling and grooming techniques.", "Beginner"),
        ("Hair Braiding", "Professional braiding techniques and styles.", "Beginner"),
        ("Makeup Artistry", "Professional makeup application techniques.", "Beginner"),
        ("Skincare", "Basic skincare and personal care practices.", "Beginner"),
        ("Nail Care", "Professional nail care and styling.", "Beginner"),
        ("Barbering", "Professional haircutting and grooming.", "Beginner"),
        ("Beauty Business", "Managing and growing a beauty service business.", "Intermediate"),
    ],

    "Home & Appliances Repairs": [
        ("Home Appliance Repair", "Diagnosing and repairing household appliances.", "Intermediate"),
        ("Refrigerator Repair", "Maintaining and repairing refrigeration systems.", "Intermediate"),
        ("Washing Machine Repair", "Diagnosing and repairing washing machines.", "Intermediate"),
        ("Air Conditioner Repair", "Maintaining and repairing air conditioning systems.", "Intermediate"),
        ("Television Repair", "Diagnosing and repairing television systems.", "Intermediate"),
        ("Water Pump Repair", "Maintaining and repairing domestic water pumps.", "Intermediate"),
        ("Furniture Repair", "Repairing and restoring household furniture.", "Beginner"),
    ],

    "Fashion Creative & Manufacturing": [
        ("Fashion Design", "Designing clothing and fashion products.", "Beginner"),
        ("Tailoring", "Professional garment construction and alteration.", "Beginner"),
        ("Pattern Making", "Creating patterns for garment production.", "Intermediate"),
        ("Leatherwork", "Creating products from leather materials.", "Beginner"),
        ("Shoemaking", "Designing and manufacturing footwear.", "Intermediate"),
        ("Bag Making", "Designing and manufacturing bags and accessories.", "Beginner"),
        ("Fashion Business", "Managing and growing a fashion business.", "Intermediate"),
        ("Textile Production", "Understanding textile materials and production.", "Intermediate"),
    ],

    "Food & Hospitality": [
        ("Cooking", "Preparing meals using professional cooking techniques.", "Beginner"),
        ("Baking", "Preparing bread, cakes and baked products.", "Beginner"),
        ("Catering", "Providing food services for events and organizations.", "Intermediate"),
        ("Food Preservation", "Preserving food safely for longer storage.", "Beginner"),
        ("Food Safety", "Applying safe food handling and hygiene practices.", "Beginner"),
        ("Hospitality Management", "Managing hospitality operations and customer experience.", "Intermediate"),
        ("Restaurant Management", "Managing restaurant operations and services.", "Intermediate"),
        ("Pastry Making", "Preparing professional pastry products.", "Intermediate"),
    ],

    "Agriculture & Animal Skills": [
        ("Crop Farming", "Planning and managing crop production.", "Beginner"),
        ("Livestock Farming", "Managing and raising farm animals.", "Beginner"),
        ("Poultry Farming", "Managing poultry production systems.", "Beginner"),
        ("Fish Farming", "Managing aquaculture and fish production.", "Beginner"),
        ("Irrigation", "Managing water systems for agricultural production.", "Intermediate"),
        ("Agricultural Technology", "Applying technology to improve agricultural production.", "Intermediate"),
        ("Food Processing", "Processing agricultural products into useful food products.", "Intermediate"),
        ("Farm Business Management", "Managing agricultural businesses and finances.", "Intermediate"),
    ],
}


def seed_skills():
    db = SessionLocal()

    try:
        created = 0
        existing = 0
        missing_categories = 0

        for category_name, skills in SKILLS.items():

            category = (
                db.query(SkillCategory)
                .filter(SkillCategory.name == category_name)
                .first()
            )

            if not category:
                print(f"WARNING: Category not found: {category_name}")
                missing_categories += 1
                continue

            for name, description, level in skills:

                skill = (
                    db.query(Skill)
                    .filter(
                        Skill.name == name,
                        Skill.category_id == category.id,
                    )
                    .first()
                )

                if skill:
                    existing += 1
                    continue

                skill = Skill(
                    name=name,
                    description=description,
                    level=level,
                    category_id=category.id,
                )

                db.add(skill)
                created += 1

        db.commit()

        total = created + existing

        print("========================================")
        print("          EarnFix Skill Seeder")
        print("========================================")
        print(f"Skills created: {created}")
        print(f"Skills already existed: {existing}")
        print(f"Skills processed: {total}")
        print(f"Missing categories: {missing_categories}")
        print("========================================")

    except Exception as error:
        db.rollback()

        print("========================================")
        print("ERROR WHILE SEEDING SKILLS")
        print("========================================")
        print(error)
        print("========================================")

        raise

    finally:
        db.close()


if __name__ == "__main__":
    seed_skills()