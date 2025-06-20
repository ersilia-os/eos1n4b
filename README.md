# Identifying HDAC3 inhibitors

The model predicts the inhibitory potential of small molecules against Histone deacetylase 3 (HDAC3), a relevant human target for cancer, inflammation, neurodegenerative diseases and diabetes. The authors have used a dataset of 1098 compounds from ChEMBL and validated the model using the benchmark MUBD-HDAC3.

This model was incorporated on 2023-12-14.

## Information
### Identifiers
- **Ersilia Identifier:** `eos1n4b`
- **Slug:** `hdac3-inhibition`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Cancer`
- **Target Organism:** `Homo sapiens`
- **Tags:** `Cancer`, `ChEMBL`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability that the molecule is a HDAC3 inhibitor

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| hdac3_inhibition_probability | float | high | Probability score of HDAC3 inhibition |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos1n4b](https://hub.docker.com/r/ersiliaos/eos1n4b)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1n4b.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1n4b.zip)

### Resource Consumption
- **Model Size (Mb):** `1`
- **Environment Size (Mb):** `984`
- **Image Size (Mb):** `967.54`

**Computational Performance (seconds):**
- 10 inputs: `30.98`
- 100 inputs: `20.86`
- 10000 inputs: `293.08`

### References
- **Source Code**: [https://github.com/jwxia2014/HDAC3i-Finder](https://github.com/jwxia2014/HDAC3i-Finder)
- **Publication**: [https://onlinelibrary.wiley.com/doi/10.1002/minf.202000105](https://onlinelibrary.wiley.com/doi/10.1002/minf.202000105)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Abellegese](https://github.com/Abellegese)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos1n4b
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos1n4b
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
