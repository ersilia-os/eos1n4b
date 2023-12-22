# Identifying HDAC3 inhibitors

The model predicts the inhibitory potential of small molecules against Histone deacetylase 3 (HDAC3), a relevant human target for cancer, inflammation, neurodegenerative diseases and diabetes. The authors have used a dataset of 1098 compounds from ChEMBL and validated the model using the benchmark MUBD-HDAC3

## Identifiers

* EOS model ID: `eos1n4b`
* Slug: `hdac3-inh`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Score`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability that the molecule is a HDAC3 inhibitor

## References

* [Publication](https://onlinelibrary.wiley.com/doi/10.1002/minf.202000105)
* [Source Code](https://github.com/jwxia2014/HDAC3i-Finder)
* Ersilia contributor: [Richiio](https://github.com/Richiio)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos1n4b)
* [AWS S3](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos1n4b.zip)
* [DockerHub](https://hub.docker.com/r/ersiliaos/eos1n4b) (AMD64)

## Citation

If you use this model, please cite the [original authors](https://onlinelibrary.wiley.com/doi/10.1002/minf.202000105) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!