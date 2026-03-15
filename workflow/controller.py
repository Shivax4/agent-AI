import json
import os
import datetime

from questions import questions


def run_interview(followup_chain, structuring_chain, insight_chain):

    conversation = []

    print("\n===== AI EXIT INTERVIEW STARTED =====\n")

    for q in questions:

        print("\nAI:", q)

        ans = input("Employee: ")

        conversation.append({
            "question": q,
            "answer": ans
        })

        # Generate follow-up question
        follow = followup_chain.invoke({"answer": ans}).strip()

        if follow.upper() != "NONE":

            print("\nAI:", follow)

            extra = input("Employee: ")

            conversation.append({
                "followup_question": follow,
                "answer": extra
            })

    # Generate structured JSON response
    structured_data = structuring_chain.invoke({
        "conversation": conversation
    })

    # Generate insights summary
    summary = insight_chain.invoke({
        "data": structured_data
    })

    print("\n===== EXIT INTERVIEW INSIGHTS =====\n")

    print(summary)

    # Ensure outputs folder exists
    os.makedirs("outputs", exist_ok=True)

    # Unique filename using timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"outputs/interview_{timestamp}.json"

    # Save final interview record
    result = {
        "conversation_transcript": conversation,
        "structured_response": structured_data,
        "insights_summary": summary
    }

    with open(filename, "w") as f:
        json.dump(result, f, indent=4)

    print(f"\nInterview saved to {filename}\n")

    return conversation