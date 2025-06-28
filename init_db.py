from app import create_app, db
from app.models import Product, Category

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Add demo categories and products
    cat = Category(name="AI Tools", type="Software", subcategories="Resume, Chatbot, Vision")
    db.session.add(cat)

    prod = Product(
        title="AI Resume Builder",
        description="Auto-generate resumes using AI.",
        price=199,
        category="AI Tools",
        subcategory="Resume",
        image_url="https://placehold.co/300x160",
        status="Available"
    )
    db.session.add(prod)

    db.session.commit()
    print("✅ Database initialized.")
    