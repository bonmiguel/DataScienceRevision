"""Starter Pandas script for the workspace."""

from __future__ import annotations

import pandas as pd


def main() -> None:
	data = {
		"name": ["Alice", "Bob", "Cara"],
		"score": [90, 85, 92],
	}

	frame = pd.DataFrame(data)
	print(frame)
	print()
	print(frame.describe())


if __name__ == "__main__":
	main()