# Bitcoin-Lite 

## Introduction

The **Bitcoin-Lite** package is a Python-based, simplified implementation of a cryptocurrency-like transaction system. It leverages **Cython** for performance optimization, making operations like creating and processing transactions significantly faster. This package is ideal for educational purposes, testing blockchain-related ideas, or understanding cryptocurrency principles in a lightweight, approachable manner.

## How it works

- **Transaction management**:
  - Creates transactions with details such as sender, receiver, and amount.
  - Generates transaction summaries quickly using optimized Cython code.

- **Performance optimization**:
  - By using Cython, the package provides enhanced computational efficiency compared to pure Python implementations.

- **Easy to use**:
  - `Bitcoin-Lite` is designed for simplicity, allowing users to easily create, process, and interact with transactions.

## Components

### 1. `Transaction` class

The core component of the package is the `Transaction` class. This class provides:

- **Attributes**:
  - `sender`: The individual or entity sending the funds.
  - `receiver`: The individual or entity receiving the funds.
  - `amount`: The amount being transferred.

- **Methods**:
  - `__init__(sender, receiver, amount)`: Initializes a transaction with the specified details.
  - `details()`: Returns a formatted string summarizing the transaction.

### Example usage
Here is a simple example of how to use the `Transaction` class:

```python
from bitcoin_lite import Transaction

# create a transaction
tx = Transaction("Alice", "Bob", 100.0)

# print transaction details
print(tx.details())
```

### Output
```
Transaction from Alice to Bob of amount 100.0
```

## Installation

To install the Bitcoin-Lite package, follow these steps:

1. Clone the repository from GitHub:
   ```bash
   git clone <your-repo-url>
   cd bitcoin-lite
   ```

2. Install the dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Build the Cython extension:
   ```bash
   poetry run python setup.py build_ext --inplace
   ```

## Testing the `Bitcoin-Lite`

You can test the package functionality using the provided test script:

```bash
poetry run python test_transaction.py
```

This will create a sample transaction and display its details.

## Contribution

Contributions to the Bitcoin-Lite package are welcome! If you have ideas for additional features, optimizations, or examples, feel free to submit a pull request or open an issue in the GitHub repository.

## License

This package will be open-source and available under the [MIT License](LICENSE).

