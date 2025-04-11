from pymongo import MongoClient
from flask_bcrypt import Bcrypt
import os

# Setup
client = MongoClient('mongodb+srv://admin:admin@cluster0.jnqzxno.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')  # Make sure MONGO_URI is set
db = client.blogDB
bcrypt = Bcrypt()



# Manually define and hash passwords
users = [
    {"username": "alice", "password": bcrypt.generate_password_hash("alice123").decode("utf-8")},
    {"username": "bob", "password": bcrypt.generate_password_hash("bob123").decode("utf-8")},
    {"username": "charlie", "password": bcrypt.generate_password_hash("charlie123").decode("utf-8")}
]

# Insert users
db.users.insert_many(users)

# Posts data
posts = [
    {
        "title": "Welcome to My Blog",
        "content": "This is the very first post on this platform. I'm incredibly excited to begin this journey into blogging. My goal is to share thoughts, tips, and insights that might help or inspire someone out there. Whether it's about technology, productivity, or just personal stories, I hope this blog becomes a meaningful space to express and connect. Stay tuned for more!",
        "author": "alice"
    },
    {
        "title": "Flask Tips & Tricks",
        "content": "Flask is a lightweight WSGI web application framework in Python that makes it easy to start simple and scale up to complex applications. Some useful tips: 1. Use `Flask Blueprints` to organize your code modularly. 2. Always configure `SECRET_KEY` for session security. 3. Use `Flask-Migrate` for database migrations. 4. Utilize `Jinja2 macros` to reuse template code. These small practices can lead to much cleaner and maintainable code as your app grows.",
        "author": "bob"
    },
    {
        "title": "Top 5 Python Libraries",
        "content": "Python’s ecosystem is huge, but here are five libraries I find myself using constantly: 1. **NumPy** for numerical operations; 2. **Pandas** for data manipulation; 3. **Requests** for HTTP operations; 4. **Flask** for web development; 5. **BeautifulSoup** for web scraping. Each library brings a powerful set of features that simplify tasks which would otherwise require a lot more code. I’ll be writing deep-dives into each of these libraries in upcoming posts!",
        "author": "charlie"
    },
    {
        "title": "MongoDB vs SQL",
        "content": "Choosing between MongoDB and a traditional SQL database depends on the use case. MongoDB, being NoSQL, excels at handling unstructured or semi-structured data and allows for fast iteration with flexible schema. SQL databases, like PostgreSQL or MySQL, enforce structured schemas and are ideal for complex relational queries and transactional integrity. In this post, I’ll walk through real-world examples, performance benchmarks, and migration tips to help you decide which suits your project best.",
        "author": "alice"
    },
    {
        "title": "Why Learn Data Structures",
        "content": "Data Structures are the building blocks of efficient software. Whether it’s searching, sorting, or managing memory, knowing which data structure to use can dramatically improve performance. Arrays, linked lists, trees, graphs, heaps—each has its strengths and ideal use cases. This post outlines practical examples, interview tips, and how to visualize these structures in your code.",
        "author": "bob"
    },
    {
        "title": "The Power of Writing Code Daily",
        "content": "Building a habit of writing code every day, even for 20 minutes, can accelerate your learning like nothing else. It keeps your problem-solving muscles sharp, helps you retain new concepts, and builds a portfolio over time. In this article, I’ll share how I built this habit, the tools I use (like LeetCode, GitHub, and VSCode), and the unexpected benefits that came from this daily practice.",
        "author": "charlie"
    }
]

# Insert posts
db.blogs.insert_many(posts)

print("Inserted users and posts successfully!")
