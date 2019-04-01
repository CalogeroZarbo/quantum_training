# D-Wave Quantum Computing playground

## D-Wave Challenges
In this folder you can find the D-Wave exercises for the D-Wave challenges pilot

## Quantum Machine Learning

### QBoost & AWS Sagemaker - Managed Training & Serving of QML models
In the folder sagemaker-qboost you can find my example on how to run the QBoost algorithm on AWS SageMaker, in order to be
a fully managed service, and therefore production ready.
In this particular example you will perform only the _training_ procedure on the D-Wave machine and then transport back the
result in the classical world to be used for inference in a classical CPU. You won't use QPU time for inference.
The tutorial is inspired by the work of D-Wave on the implementation of the [QBoost][qbst] algorithm, and by the official
tutorial of AWS SageMaker [Bring Your Own Algorithm][aws_sgmkr].


[qbst]: https://github.com/dwavesystems/qboost "D-Wave QBoost GitHub page"
[aws_sgmkr]: http://scikit-learn.org "AWS SageMaker scikit-learn tutorial"
