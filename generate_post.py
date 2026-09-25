import os
import random
import datetime

AFFILIATE_TAG = "senthil4u-21"

PET_TOPICS = [
    {
        "title": "How AI Is Solving Separation Anxiety in Household Dogs",
        "category": "Dog Tech & Behavior",
        "asin": "B07232M876",
        "pain_point": "Separation anxiety, excessive barking, and destructive behavior when owners leave home.",
        "solution": "Smart AI pet cameras with real-time barking recognition and automatic treat dispensation."
    },
    {
        "title": "Automated Health Monitoring: How Smart Feeders Prevent Pet Obesity",
        "category": "Cat & Dog Nutrition",
        "asin": "B08N5WRWNW",
        "pain_point": "Irregular feeding schedules, overfeeding, and multi-pet food theft.",
        "solution": "Microchip-activated smart feeders with precision portion control and mobile app monitoring."
    }
]

def generate_humanized_article():
    topic = random.choice(PET_TOPICS)
    today = datetime.date.today().strftime("%B %d, %Y")
    
    markdown_content = f"""# {topic['title']}
*Published on {today} | Category: {topic['category']}*

### Addressing the Root Pain Point
Every pet owner faces moments of doubt regarding their pet's health and happiness. One major daily struggle is **{topic['pain_point']}**

### The AI-Driven Solution
Modern smart pet gear uses automated sensors to resolve this issue:
- **Real-Time Data:** {topic['solution']}
- **Stress Reduction:** Minimizes anxiety for both pets and owners.
- **Convenience:** Keeps your pet's schedule consistent regardless of your work routine.

---

### Recommended Tool for Pet Parents
If you want to simplify your daily routine while keeping your pet safe:

[Check Official Amazon Listing & Current Pricing](https://www.amazon.com/dp/{topic['asin']}?tag={AFFILIATE_TAG})
"""

    with open("latest_post.md", "w", encoding="utf-8") as f:
        f.write(markdown_content)
    print("Pet care humanized article generated successfully.")

if __name__ == "__main__":
    generate_humanized_article()
