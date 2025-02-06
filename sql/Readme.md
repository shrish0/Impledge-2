# Approach

### first solution
we just combine the admission and doctor table and select the doctor table attribute to get information on which doctor have admission as when we do a join it will only join attribute which satisfy the join condition

### second solution
to find doctor who doesnt have admission 
we done a left join where doctor are on the left side so if thier is no admission.doctot_attending_id it will null thier for doctors than we smartly apply a condition where attending id is null

### third solution
in third we have to find about the condition where the doctor record is missing in doctors table but it allottedin admission.attending_doctor id
so we first join patient and admission
then we left join admission with doctor
and we apply a condition when doctor id is null as we apply left join so when thier is no record for admission it filled with null and thats how we get our result