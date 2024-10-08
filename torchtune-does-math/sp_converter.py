import json


def main():
    with open("/data/users/ebs/tuneathon-ckpts/base-model/tokenizer.json") as f:
        tokenizer_cfg = json.load(f)
    vocab = tokenizer_cfg["model"]["vocab"]
    merges = tokenizer_cfg["model"]["merges"]
    with open("/data/users/ebs/tuneathon-ckpts/base-model/vocab.json", "w") as outfile:
        json.dump(vocab, outfile)
    with open("/data/users/ebs/tuneathon-ckpts/base-model/merges.txt", "w") as f:
        for merge in merges:
            f.write(f"{merge}\n")


if __name__ == "__main__":
    main()
