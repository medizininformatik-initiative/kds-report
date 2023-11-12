# KDS Report 2.0

The new version of the KDS report will include a json schema, which defines it clearly.

The new version will allow 2 types of query.
A count query and a year query.

A count query is a query which counts the number of overall resources of a type or profile.
A year query is a query which counts the number of overall resources per year of a type of profile for all years since 2000 in yearly steps.

The following regex describes the allowed urls that can be used as part of the report input-queries:
```
^(((?!=)|_profile=|_profile:below=|type=|date=[0-9]{4}(?![-])).)*_summary=count
```

## Counting queries

A count query can be identified by ending wit _summary=count.
Further the other allowed params should be type and date. 


## Counting for year queries

The counting for year queries will begin in the year 2000 and only counts of date parameters are allowed which use the eq comparator and are restricted to the year.
For the DSF version - the original response and request will have a one query per year.

## Counting Encounter (Fall) instead of patient

Instead of counting patients per year we will count the Encounter, as a count for an encounter can be written as one FHIR search query.

## Time taken

Time taken will not be measured, as the time taken for count queries does not let one extrapolate to other type of queries like
paging through results or CQL execution, making the measurement of the time taken for the KDS report queries uninformative.


# filenmae on server timestamp of report

The exact time of when the report was created will be part of the report json in the field: datetime
When saving the report the name will be as follows:
kds-report-`SITENAME`-`DATE_DAY_ACCURATE`.json
