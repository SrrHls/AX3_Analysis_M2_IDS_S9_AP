# README
This work propose a method to extract from acceleration data, recorded during walking and running at different speeds, the burned energy estimated on MET based on the bibliography element.

We used 6 differents speeds for our experiment. After regular preprocessing and based on this experiment we find out to extrapolate (based on a linear regression process) the burning energy in MET. We can now, knowing informations about the subjet, define burning calories during an exercise.
Our model provide great results for walking at a speed higer than 4 kilometers per hour, many things can explain this result : 
  Not enough data for the low walking speed
  When walking the swinging arms is different than running, it can causes miss calculation by the model
  Not enough subjets, we built this method on only one subject
