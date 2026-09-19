# house-management

A small tool to manage moving-related inventory, budgets, vendors, and timelines. See .planning/ for project plans and requirements.

## TODO

- [ ] Evaluate scalable PDF table extraction options:
  - **[Docling](https://docling-project.github.io/docling/usage/advanced_options/):** automatic layout and table-structure recognition without per-file coordinates.
  - **[pdfplumber](https://github.com/jsvine/pdfplumber#table-extraction-settings):** automatic alignment-based table detection, with heuristics to group wrapped descriptions into logical rows.
- [ ] Benchmark both options on the your quotation PDFs before choosing or replacing the current extractor. Check row/cell accuracy, wrapped descriptions, optional items (`10b`, `12b`), separately priced subrows, unnumbered labour charges, blank totals, and `Bundle` prices. Compare runtime and setup requirements, and preserve quantity/price associations in both structured and readable output.
