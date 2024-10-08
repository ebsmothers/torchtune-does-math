import json


# We have to do this first because not all samples have a unique proof
def main():
    data_dir = "/data/users/ebs/naturalproofsdata"
    splits = ["proofwiki", "stack", "stein", "trench"]
    datasets = {}
    for split in splits:
        fname = f"{data_dir}/naturalproofs_{split}.json"
        with open(fname, "r") as f:
            datasets[split] = json.load(f)

    # Throwing out a lot of stuff but this is a good start
    for split in splits:
        dataset = []
        for sample in datasets[split]["dataset"]["theorems"]:
            for proof in sample["proofs"]:
                dataset.append(
                    {
                        "theorem": "\n".join(sample["contents"]),
                        "proof": "\n".join(proof["contents"]),
                    }
                )
        fname = f"{data_dir}/naturalproofs_{split}_cleaned.json"
        with open(fname, "w") as f:
            json.dump(dataset, f)


if __name__ == "__main__":
    main()
