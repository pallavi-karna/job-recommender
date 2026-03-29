import pandas as pd

# load dataset
data = pd.read_csv("jobs.csv")

# function to recommend jobs
def recommend_jobs(user_skills):
    results = []

    for index, row in data.iterrows():
        description = row['Job Description'].lower()

        match_count = 0

        for skill in user_skills:
            if skill.lower() in description:
                match_count += 1

        if match_count > 0:
            results.append((row['Job Title'], match_count))

    # sort by match count
    results.sort(key=lambda x: x[1], reverse=True)

    return results[:5]


# test the system
user_input = input("Enter your skills (comma separated): ")
skills = user_input.split(",")

recommended = recommend_jobs(skills)

if not recommended:
    print("No matching jobs found")
else:
    print("\nRecommended Jobs:")
    for job, score in recommended:
        print(f"{job} (match score: {score})")