from tokenizer import DeepSeekTokenizer
from torchtune.data import PromptTemplate
from torchtune.datasets import instruct_dataset
from torchtune.models.gemma import gemma_tokenizer


def deepseek_template() -> PromptTemplate:
    return PromptTemplate(
        template={
            "user": (
                "User: ",
                "\nPlease reason step by step, and put your final answer within \\boxed{}.",
            ),
            "assistant": ("Assistant: ", "\n"),
        },
    )


tokenizer = DeepSeekTokenizer(
    path="/data/users/ebs/tuneathon-ckpts/base-model/vocab.json",
    merges_file="/data/users/ebs/tuneathon-ckpts/base-model/merges.txt",
    prompt_template="dataset.DeepSeekPromptTemplate",
    max_seq_len=4096,
)

ds = instruct_dataset(
    tokenizer=tokenizer,
    source="wellecks/naturalproofs-gen",
    data_files="data/my_data.csv",
    split="train",
    # By default, user prompt is ignored in loss. Set to True to include it
    train_on_input=False,
    # According to DeepSeek we don't want system prompt?
    # new_system_prompt="You are an AI assistant. ",
    # Use columns in our dataset instead of default
    column_map={"input": "incorrect", "output": "correct"},
    verification_mode=VerificationMode.NO_CHECKS,  # need this for some reason
)
