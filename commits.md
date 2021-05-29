### **05/24/2021**
- Initial commit
    - Creates and clones the repository
- Creates file structure
    - Adds [commits](commits.md)
    - Adds [Resources](Resources) folder
    - Adds [climate_starter](climate_starter.ipynb), [temp_analysis_bonus_1_starter](temp_analysis_bonus_1_starter.ipynb) and [temp_analysis_bonus_2_starter](temp_analysis_bonus_2_starter.ipynb)
- Updates readme
    - Adds task list to readme
- Links database
    - Step 1 Preparation tasks
- Finds last date
    - Queries the DB to find the last measurement date
- Computes time delta
    - Adds leap-year logic
- Computes precipitation analysis
    - [X] Graphic looks weird, needs debugging

### **05/26/2021**
- Fixes precipitation graph
    - Changes the graph style to a pandas plot

### **05/27/2021**
- Adds station queries

### **05/28/2021**
- Adds query to find most active station
- Adds station histogram
- Adds flask API general layout
- Fixes bug on leap-year calculations
- Adds /stations and /tobs to API

### **05/29/2021**
- Adds /\<start> and /\<start> /\<end> endpoints to API
- Reformats all json to dictionaries and column names
- Adds temperature analysis t-test