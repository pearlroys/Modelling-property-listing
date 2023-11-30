We conducted an investigation and implemented a solution to align the baseline calculator 
with the optimiser's assumptions regarding state of charge (SOC) after a full outage. 
This corrective measure aims to prevent the defaulting behavior that previously caused the issue. 
The fix has been applied by disabling the emergency baselining behavior of the baseline calculator for the optimiser,
 mitigating the risk of conflicts between the two. The solution is now in production, and we 
will monitor its performance throughout the afternoon to ensure there are no further issues.