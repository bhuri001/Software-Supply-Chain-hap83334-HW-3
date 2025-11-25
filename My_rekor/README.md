# Python Rekor Verifier

Introducing a powerful command-line tool explicitly designed for efficiently querying and verifying entries in a Rekor transparency log. With this tool, you can seamlessly fetch log entries, confidently verify inclusion proofs, and reliably check the consistency of the log's Merkle tree.

## Description

This project offers a robust client for interacting directly with a Rekor server (e.g., `https://rekor.sigstore.dev`).

### Key Features

- Effortlessly fetch log entries by index.
- Unquestionably verify artifact signatures using public keys from log entries.
- Conduct inclusion proof verification to ensure that an entry is securely within the log.
- Guarantee consistency between an old tree state and a new one with absolute confidence.

## Installation

1. Install the required dependencies:
    ```bash
    pip install poetry
    poetry install
    ```

## Usage

Harness the power of this tool directly from the command line.

### Get Latest Checkpoint

Easily retrieve the latest signed tree head (checkpoint) from the Rekor server:
```bash
python main.py --checkpoint
```

### Verify Inclusion

Confidently verify that an artifact is included in the log at a specified index. Simply provide the log index and the path to the original artifact:

```bash
python main.py --inclusion <LOG_INDEX> --artifact <PATH_TO_ARTIFACT>
```

**Example:**
```bash
python main.py --inclusion 12345 --artifact ./my-file.txt
```

### Verify Consistency

Ensure that your previously known checkpoint is consistent with the latest checkpoint. Gather the `treeID`, `treeSize`, and `rootHash` from the old checkpoint for this verification:

```bash
python main.py --consistency --tree-id <TREE_ID> --tree-size <OLD_TREE_SIZE> --root-hash <OLD_ROOT_HASH>
```

**Example:**
```bash
python main.py --consistency --tree-id 238498... --tree-size 1000 --root-hash abcdef123...
```

### Debug Mode

For detailed and verbose output for any command, confidently use the `--debug` or `-d` flag:
```bash
python main.py --checkpoint --debug
```

Get ready to take control of your log verification processes with the Python Rekor Verifier!
