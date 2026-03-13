#!/usr/bin/env python3
"""
Seed script for Portfolio Backend database.
Populates your actual portfolio data for About, Skills, Experiences, Projects.
Run after server startup: cd portfolio_backend_fastapi && python seed_data.py
"""

import asyncio
import json
from datetime import date
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession
from app.config.database import AsyncSessionLocal, Base
from app.models.sql_models import AboutModel, SkillModel, ExperienceModel, ProjectModel
from app.config.settings import settings

async def seed_about(session: AsyncSession):
    # Clear existing
    await session.execute(AboutModel.__table__.delete())
    
    about_data = {
        "name": "Raj Shekhar Singh",
        "title": "Full-Stack Developer and AI Engineer",
        "bio": "I build scalable full-stack and AI-powered systems that turn complex data into intelligent, real-world applications and actionable insights. I design and develop high-performance platforms using React, Next.js, Spring Boot, FastAPI, Python, and Java, integrating advanced AI techniques such as RAG pipelines, vector search, and intelligent automation. At Infosys, I engineered large-scale Apache Spark and Kafka data pipelines on Azure Data Lake, improving real-time data processing performance, and I continue to build production-grade AI, SaaS, and data engineering platforms focused on scalability, performance, and real-world impact.",
        "email": "rajsingh170901@gmail.com",
        "phone": "+91-XXXXXXXXXX",
        "location": "Bangalore, India",
        "profile_image": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=500",
        "resume_url": "https://rajshekhar.live/resume.pdf",
        "github_url": "https://github.com/regalleo",
        "linkedin_url": "https://www.linkedin.com/in/raj-shekhar-singh-aa16ab245/",
        "twitter_url": "https://twitter.com/rajshekharsingh"
    }
    stmt = insert(AboutModel).values(**about_data)
    await session.execute(stmt)
    print("✅ Seeded About data")

async def seed_skills(session: AsyncSession):
    await session.execute(SkillModel.__table__.delete())
    
    skills = [
        {'name': 'Python', 'category': 'Backend', 'proficiency': 95, 'years_of_experience': 4, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/python.svg'},
        {'name': 'FastAPI', 'category': 'Backend', 'proficiency': 90, 'years_of_experience': 3, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/fastapi.svg'},
        {'name': 'React', 'category': 'Frontend', 'proficiency': 85, 'years_of_experience': 3, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/react.svg'},
        {'name': 'Next.js', 'category': 'Frontend', 'proficiency': 85, 'years_of_experience': 2, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/nextdotjs.svg'},
        {'name': 'Spring Boot', 'category': 'Backend', 'proficiency': 80, 'years_of_experience': 2, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/springboot.svg'},
        {'name': 'Java', 'category': 'Backend', 'proficiency': 80, 'years_of_experience': 2, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/java.svg'},
        {'name': 'JavaScript', 'category': 'Frontend', 'proficiency': 90, 'years_of_experience': 4, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/javascript.svg'},
        {'name': 'TypeScript', 'category': 'Frontend', 'proficiency': 85, 'years_of_experience': 2, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/typescript.svg'},
        {'name': 'PostgreSQL', 'category': 'Database', 'proficiency': 85, 'years_of_experience': 3, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/postgresql.svg'},
        {'name': 'MongoDB', 'category': 'Database', 'proficiency': 80, 'years_of_experience': 2, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/mongodb.svg'},
        {'name': 'Apache Spark', 'category': 'Big Data', 'proficiency': 75, 'years_of_experience': 1, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/apache.svg'},
        {'name': 'Kafka', 'category': 'Big Data', 'proficiency': 75, 'years_of_experience': 1, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/apachekafka.svg'},
        {'name': 'Docker', 'category': 'DevOps', 'proficiency': 80, 'years_of_experience': 2, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/docker.svg'},
        {'name': 'Azure', 'category': 'Cloud', 'proficiency': 75, 'years_of_experience': 1, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/microsoftazure.svg'},
        {'name': 'LangChain', 'category': 'AI/ML', 'proficiency': 80, 'years_of_experience': 1, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/langchain.svg'},
        {'name': 'AI Agents', 'category': 'AI/ML', 'proficiency': 80, 'years_of_experience': 1, 'icon_url': 'https://cdn.jsdelivr.net/npm/simple-icons@v8/icons/huggingface.svg'},
    ]
    for skill in skills:
        stmt = insert(SkillModel).values(**skill)
        await session.execute(stmt)
    print(f"✅ Seeded {len(skills)} Skills")

async def seed_experiences(session: AsyncSession):
    await session.execute(ExperienceModel.__table__.delete())
    
    experiences = [
        {
            'company': 'Infosys Limited',
            'position': 'Specialist Programmer Level 1',
            'description': 'Architected and optimized large-scale ETL pipelines on Azure Data Lake using Apache Spark and Kafka, reducing processing latency by 35% and increasing throughput by 40%. Built real-time data processing systems integrating MongoDB, MySQL, and NoSQL platforms for scalable analytics.',
            'start_date': date(2025, 6, 1),
            'end_date': date(2025, 9, 1),
            'current': False,
            'location': 'Mysuru, India',
            'achievements': json.dumps([
                'Reduced processing latency by 35%',
                'Increased throughput by 40%',
                'Implemented Generative AI-driven analytics automation, reducing reporting time by 30%',
                'Collaborated in Agile Scrum teams with CI/CD pipelines, accelerating deployment cycles by 25%'
            ])
        },
        {
            'company': 'Surat Construction Pvt. Ltd.',
            'position': 'Data Analytics Intern',
            'description': 'Managed and optimized SQL-driven databases for construction assets, procurement, and project cost tracking.',
            'start_date': date(2025, 1, 1),
            'end_date': date(2025, 6, 1),
            'current': False,
            'location': 'Lucknow, India',
            'achievements': json.dumps([
                'Improved analytical query performance by up to 35% through database optimization and indexing strategies',
                'Built Python analytics pipelines using Pandas and Matplotlib to generate actionable insights for management'
            ])
        },
        {
            'company': 'CodeClause',
            'position': 'Data Science Intern',
            'description': 'Developed and deployed machine learning models for fraud detection and data analysis.',
            'start_date': date(2024, 6, 1),
            'end_date': date(2024, 12, 1),
            'current': False,
            'location': 'Remote',
            'achievements': json.dumps([
                'Developed and deployed machine learning models for fraud detection, achieving 99.6% accuracy on credit card transaction datasets',
                'Built data preprocessing and model training pipelines using Python, Pandas, and Scikit-learn',
                'Implemented data analysis and visualization workflows to uncover patterns, anomalies, and predictive insights'
            ])
        }
    ]
    for exp in experiences:
        stmt = insert(ExperienceModel).values(**exp)
        await session.execute(stmt)
    print(f"✅ Seeded {len(experiences)} Experiences")

async def seed_projects(session: AsyncSession):
    await session.execute(ProjectModel.__table__.delete())
    
    projects = [
        {
            'title': 'AI Data Analyst Platform',
            'description': 'An AI-powered analytics platform that automatically cleans datasets, generates visualizations, and answers natural language questions about data.',
            'image_url': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=500',
            'github_link': 'https://github.com/regalleo/ai-data-analyst',
            'live_link': 'https://ai-data-analyst-lac.vercel.app/',
            'technologies': json.dumps(['FastAPI', 'Next.js', 'LangChain', 'PostgreSQL', 'AI Agents']),
            'category': 'AI/ML',
            'completed_date': date(2024, 12, 1),
            'featured': True
        },
        {
            'title': 'Customer 360 Analytics Platform',
            'description': 'A large-scale analytics platform that unifies data from multiple sources and enables real-time customer insights.',
            'image_url': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=500',
            'github_link': 'https://github.com/regalleo/customer360-platform',
            'live_link': 'https://customer360-brxq.onrender.com/',
            'technologies': json.dumps(['MongoDB', 'Apache Spark', 'Kafka', 'Hadoop', 'Azure Data Lake']),
            'category': 'Big Data',
            'completed_date': date(2024, 10, 15),
            'featured': True
        },
        {
            'title': 'Task Manager Dashboard',
            'description': 'A full-stack productivity application for task management with AI-assisted suggestions.',
            'image_url': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=500',
            'github_link': 'https://github.com/regalleo/springboot_django_full_stack',
            'live_link': 'https://springboot-django-full-stack-2.onrender.com/',
            'technologies': json.dumps(['Spring Boot', 'Django', 'JavaScript', 'Bootstrap', 'REST APIs']),
            'category': 'Full Stack',
            'completed_date': date(2024, 8, 20),
            'featured': False
        },
        {
            'title': 'Tasks Generator – AI Project Planner',
            'description': 'An AI-powered tool that converts product ideas into structured user stories and engineering tasks.',
            'image_url': 'https://images.unsplash.com/photo-1456324504439-367cee3b3c32?w=500',
            'github_link': 'https://github.com/regalleo/tasks-generator-app',
            'live_link': 'https://tasks-generator-app-udu5-crv5nm19w-rajs-projects-020404b6.vercel.app/',
            'technologies': json.dumps(['Next.js', 'AI APIs', 'React', 'Tailwind CSS']),
            'category': 'AI/ML',
            'completed_date': date(2024, 7, 10),
            'featured': False
        },
        {
            'title': 'Smart Bookmarks',
            'description': 'A real-time bookmark manager with secure authentication and synchronized updates across sessions.',
            'image_url': 'https://images.unsplash.com/photo-1555421689-492a6c3d3e69?w=500',
            'github_link': 'https://github.com/regalleo/smart-bookmark-app',
            'live_link': 'https://smart-bookmark-app-five-beta.vercel.app/',
            'technologies': json.dumps(['Next.js', 'Supabase', 'TypeScript', 'Tailwind CSS']),
            'category': 'Frontend',
            'completed_date': date(2024, 5, 15),
            'featured': False
        },
        {
            'title': 'LeaveFlow – Leave Management System',
            'description': 'A full-stack leave management system for organizations to manage employee leave requests.',
            'image_url': 'https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=500',
            'github_link': 'https://github.com/regalleo/leave-management-web-app',
            'live_link': 'https://leave-management-web-app.vercel.app/',
            'technologies': json.dumps(['Vue.js', 'FastAPI', 'MongoDB', 'Tailwind CSS']),
            'category': 'Full Stack',
            'completed_date': date(2024, 3, 20),
            'featured': False
        },
        {
            'title': 'Dispatch Load Balancer',
            'description': 'A logistics optimization API that assigns delivery orders to vehicles while minimizing total travel distance.',
            'image_url': 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?w=500',
            'github_link': 'https://github.com/regalleo/dispatch-load-balancer',
            'live_link': None,
            'technologies': json.dumps(['Spring Boot', 'Java', 'Optimization Algorithms']),
            'category': 'Backend',
            'completed_date': date(2024, 1, 10),
            'featured': False
        },
        {
            'title': 'Transporter Assignment Optimizer',
            'description': 'A logistics optimization application that assigns transporters to shipping lanes while minimizing operational cost.',
            'image_url': 'https://images.unsplash.com/photo-1587293852726-70cdb56c2866?w=500',
            'github_link': 'https://github.com/regalleo/transporter-assignment',
            'live_link': None,
            'technologies': json.dumps(['Spring Boot', 'Java', 'H2 Database', 'JPA']),
            'category': 'Backend',
            'completed_date': date(2023, 11, 5),
            'featured': False
        },
        {
            'title': 'Voice KYC Bot',
            'description': 'A voice-based AI assistant that simulates KYC verification calls for fintech customer onboarding.',
            'image_url': 'https://images.unsplash.com/photo-1589254065878-42c9da997008?w=500',
            'github_link': 'https://github.com/regalleo/Voice-KYC-Bot',
            'live_link': None,
            'technologies': json.dumps(['Python', 'Speech Recognition', 'TTS APIs']),
            'category': 'AI/ML',
            'completed_date': date(2023, 9, 1),
            'featured': False
        },
        {
            'title': 'Portfolio Website',
            'description': 'A modern developer portfolio showcasing projects, skills, and AI capabilities.',
            'image_url': 'https://images.unsplash.com/photo-1516321310764-9f3c3798b8bd?w=500',
            'github_link': 'https://github.com/regalleo/portfolio-frontend',
            'live_link': 'https://raj-shekhar-portfolio.netlify.app/',
            'technologies': json.dumps(['React', 'Tailwind CSS', 'Framer Motion']),
            'category': 'Frontend',
            'completed_date': date(2023, 6, 15),
            'featured': True
        }
    ]
    for proj in projects:
        stmt = insert(ProjectModel).values(**proj)
        await session.execute(stmt)
    print(f"✅ Seeded {len(projects)} Projects")

async def main():
    print("🌱 Starting database seeding with your portfolio data...")
    print(f"📁 Database: {settings.DATABASE_URL}")
    
    async with AsyncSessionLocal() as session:
        await seed_about(session)
        await seed_skills(session)
        await seed_experiences(session)
        await seed_projects(session)
        await session.commit()
    
    print("🎉 Seeding completed successfully!")
    print("🔍 Verify: curl http://localhost:8080/api/about/")

if __name__ == "__main__":
    asyncio.run(main())
