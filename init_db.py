from app import create_app, db
from app.models import Category, Product

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create default categories
    categories = [
        Category(
            name="Software",
            subcategories=["Python Software", "React Software", "Java Software"],
            type="software"
        ),
        Category(
            name="Projects",
            subcategories=["Python Projects", "Web Projects", "AI/ML Projects"],
            type="projects"
        ),
        Category(
            name="Apps",
            subcategories=["Android Apps", "iOS Apps", "Web Apps"],
            type="apps"
        ),
        Category(
            name="Games",
            subcategories=["Racing", "Puzzle", "Shooting", "Strategy"],
            type="games"
        )
    ]

    db.session.add_all(categories)

    # Add sample products
    products = [
        Product(
            title="Python Invoice Generator",
            description="A full Python project that generates invoices with PDF export.",
            price=499.00,
            category="Software",
            subcategory="Python Software",
            image_url="https://via.placeholder.com/300x200.png?text=Python+Invoice"
        ),
        Product(
            title="React Task Manager",
            description="A React-based task manager with drag & drop and local storage.",
            price=799.00,
            category="Software",
            subcategory="React Software",
            image_url="https://via.placeholder.com/300x200.png?text=React+Task+Manager"
        ),
        Product(
            title="Racing Game Engine",
            description="A 2D racing game made with Pygame. Great for learning game dev.",
            price=299.00,
            category="Games",
            subcategory="Racing",
            image_url="https://via.placeholder.com/300x200.png?text=Racing+Game"
        )
    ]

    db.session.add_all(products)
    db.session.commit()

    print("✅ Database initialized with categories and sample products.")
