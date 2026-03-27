from src.pipeline import run_pipeline

# 🔥 25 REQUIRED TEST QUERIES

test_cases = [
    # ✅ 1. Prerequisite checks (10)
    {"q": "Can I take CS301 after CS101?", "type": "prereq"},
    {"q": "Can I take CS202 after CS102?", "type": "prereq"},
    {"q": "Is CS303 allowed without CS202?", "type": "prereq"},
    {"q": "Can I enroll in CS307 after CS306?", "type": "prereq"},
    {"q": "Can I take CS302 without CS202?", "type": "prereq"},
    {"q": "Is MATH201 required before CS303?", "type": "prereq"},
    {"q": "Can I skip CS102?", "type": "prereq"},
    {"q": "Do I need CS101 for CS202?", "type": "prereq"},
    {"q": "Can I take CS304 after CS202?", "type": "prereq"},
    {"q": "Is CS305 allowed without CS202?", "type": "prereq"},

    # ✅ 2. Chain reasoning (5)
    {"q": "What do I need before CS307?", "type": "chain"},
    {"q": "Prerequisites for CS303?", "type": "chain"},
    {"q": "Course path to Machine Learning?", "type": "chain"},
    {"q": "Steps before Database Systems?", "type": "chain"},
    {"q": "Full chain for CS304?", "type": "chain"},

    # ✅ 3. Program requirements (5)
    {"q": "What courses are required for Computer Science degree?", "type": "program"},
    {"q": "What electives are allowed?", "type": "program"},
    {"q": "How many credits are required to graduate?", "type": "program"},
    {"q": "What math courses are required?", "type": "program"},
    {"q": "List core courses for CS program", "type": "program"},

    # ✅ 4. Not in docs / trick (5)
    {"q": "Which semester is CS303 offered?", "type": "unknown"},
    {"q": "Who teaches CS202?", "type": "unknown"},
    {"q": "What time is CS101?", "type": "unknown"},
    {"q": "Is CS303 available online?", "type": "unknown"},
    {"q": "Can professor override prerequisites?", "type": "unknown"},
]


# 🔥 STUDENT PROFILE (can change for testing)
student_profile = {
    "completed_courses": "CS101",
    "target_program": "Computer Science"
}


def evaluate():
    total = len(test_cases)
    with_citations = 0
    abstentions = 0

    print("\n🚀 RUNNING EVALUATION...\n")

    for i, test in enumerate(test_cases, 1):
        q = test["q"]

        print("=" * 80)
        print(f"Q{i}: {q}")

        try:
            result = run_pipeline(student_profile, q)
            print(result)

            # ✅ Simple checks
            if "Citations:" in result:
                with_citations += 1

            if "I don’t have that information" in result:
                abstentions += 1

        except Exception as e:
            print("❌ Error:", e)

    print("\n" + "=" * 80)
    print("📊 EVALUATION SUMMARY")
    print("=" * 80)

    print(f"Total Queries: {total}")
    print(f"Citation Coverage: {(with_citations/total)*100:.2f}%")
    print(f"Abstention Count: {abstentions} / 5 (expected for unknown queries)")

    print("\n✅ Done!")


if __name__ == "__main__":
    evaluate()