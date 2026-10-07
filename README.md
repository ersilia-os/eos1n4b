# Identifying HDAC3 inhibitors

Screens compounds for inhibition of histone deacetylase 3, a target in cancer, chronic inflammation, neurodegeneration and diabetes that no machine learning model had addressed before. Li and colleagues drew 1,098 HDAC3-assayed compounds from ChEMBL, calling anything with IC50 at or below 1 micromolar active, and compared fifteen combinations of five algorithms with Mordred descriptors, MACCS keys and Morgan2 fingerprints. XGBoost on 1024-bit Morgan2 fingerprints won and is the checkpoint served here, benchmarked on the unbiased MUBD-HDAC3 decoy set.

This model was incorporated on 2023-12-14.Last packaged on 2025-10-10.

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
- **Interpretation:** Probability that a compound inhibits histone deacetylase 3 with IC50 at or below 1 micromolar.

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
- **Environment Size (Mb):** `1021`
- **Image Size (Mb):** `1002.77`

**Computational Performance (seconds):**
- 10 inputs: `27.45`
- 100 inputs: `17.22`
- 10000 inputs: `56.57`

### References
- **Source Code**: [https://github.com/jwxia2014/HDAC3i-Finder](https://github.com/jwxia2014/HDAC3i-Finder)
- **Publication**: [https://doi.org/10.1002/minf.202000105](https://doi.org/10.1002/minf.202000105)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Richiio](https://github.com/Richiio)

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
