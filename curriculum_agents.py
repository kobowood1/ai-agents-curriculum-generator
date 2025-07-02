import os
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from agents import Agent, Runner, trace

# Load environment variables
load_dotenv()


# Agent 1: Generate learning plan
curriculum_agent = Agent(
    name="curriculum_agent",
    instructions="Generate a structured curriculum outline to help someone achieve the programming learning goal they provide.",
)

# Output schema for the curriculum checker
class CurriculumCheckOutput(BaseModel):
    good_quality: bool
    matches_goal: bool

# Agent 2: Evaluate learning plan
curriculum_checker_agent = Agent(
    name="curriculum_checker_agent",
    instructions="Evaluate the provided curriculum outline. Determine if it is high quality and if it matches the user’s learning goal.",
    output_type=CurriculumCheckOutput,
)

# Agent 3: Generate full lessons for each section
lesson_writer_agent = Agent(
    name="lesson_writer_agent",
    instructions="Write a detailed coding lesson for each section in the curriculum outline. Include explanations, code examples, and one practice question per section.",
    output_type=str,
)


async def main():
    learning_goal = input("What do you want to learn? ")

    with trace("Deterministic tutor flow"):
        # 1. Generate curriculum
        curriculum_result = await Runner.run(
            curriculum_agent,
            learning_goal,
        )
        print("\nCurriculum generated.")

        # 2. Check the curriculum
        check_result = await Runner.run(
            curriculum_checker_agent,
            curriculum_result.final_output,
        )

        assert isinstance(check_result.final_output, CurriculumCheckOutput)
        if not check_result.final_output.good_quality:
            print("Curriculum is low quality. Stopping.")
            exit(0)

        if not check_result.final_output.matches_goal:
            print("Curriculum doesn't match the learning goal. Stopping.")
            exit(0)

        print("Curriculum looks good. Proceeding to generate lessons...")

        # 3. Generate lessons
        lessons_result = await Runner.run(
            lesson_writer_agent,
            curriculum_result.final_output,
        )
        print(f"\nGenerated Lessons:\n{lessons_result.final_output}")


if __name__ == "__main__":
    asyncio.run(main())