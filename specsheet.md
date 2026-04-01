\> MediDB Specsheet revision 2.6
\> by @voxvoltera & @lilleole      
\> latest update: 01/04/2026      
    
"""
```{=latex}
\newpage
```
"""

# Revision notes      
Replaced all get with post 

# Purpose      
The purpose of this document is to be the singular source of truth for both frontend and backend development.      
It aims to prevent either team from blocking one another, or having to wait for a certain feature to be implemented before they can start their work.      
Any deviation from this document should only happen after consulting with any of the document maintainers, and subsequent updating of the specifications.    
    
# Usage      
This specsheet is to be viewed as a reference manual rather than a todo list.      
Implementation order is dictated by the Kanban board, and the order in which tickets are listed. Each Kanban ticket will map to a specific entry in this specsheet (e.g. [2.3.7]) to ensure the implementation matches the design, and is carried out in the correct order in accordance to testing efforts.    

# Database      
## CCR (Central Clinic Register)    

```{=latex}  
\begin{tiny}  
```  
```md  
| Column name | Type   | Constraints                               | Description                     | Note                                       |  
| ----------- | ------ | ----------------------------------------- | ------------------------------- | ------------------------------------------ |  
| UUID        | UUID   | PRIMARY KEY                               | UUID of clinic                  |                                            |  
| NAME        | TEXT   | NOT NULL. CHECK (LENGTH(NAME) < 1000)     | Name of clinic                  |                                            |  
| LOCATION    | TEXT   | NOT NULL. CHECK (LENGTH(LOCATION) < 1000) | Geographical location of clinic |                                            |  
| EMAIL       | TEXT   | CHECK (LENGTH(EMAIL) < 100)               | Email of clinic                 |                                            |  
| CVR         | INTGER | NOT NULL. 0-99999999                      | CVR number of clinic            | fallback if mail doesn't exist             |  
| PHONE       | INTGER | NOT NULL. 0-99999999                      | Phone number of clinic          | Assumes all phone numbers are danish (+45) |  
```  
```{=latex}  
\end{tiny}  
```  
## CUR (Central User Register)     
```{=latex}  
\begin{tiny}  
```  
```md  
| Column name | Type | Constraints                          | Description                             | Note                                                       |  
| ----------- | ---- | ------------------------------------ | --------------------------------------- | ---------------------------------------------------------- |  
| UUID        | UUID | PRIMARY KEY                          | UUID of user                            |                                                            |  
| EMAIL       | TEXT | NOT NULL. CHECK(LENGTH(EMAIL) < 200) | Email of user                           |                                                            |  
| PASSWORD    | TEXT | NOT NULL                             | Password of user                        | Should be hashed with argon2id                             |  
| SALT        | TEXT | NOT NULL                             | Salt for Argon2ID password hashing algo |                                                            |  
| NAME        | TEXT | NOT NULL. CHECK(LENGTH(NAME) < 1000) | Name of user                            |                                                            |  
| POSITION    | POS  | NOT NULL                             | Position of user                        | Position as enum. Position will also determin admin rights |  
| PFP         | TEXT |                                      | Profile picture of user                 | Storage path to PFP                                        |  
| CLINIC      | UUID | FOREIGN KEY                          | Clinic associated with user             |                                                            |  
| PHONE       | INT  | NOT NULL. 0-99999999                 | Phone number of user                    | Assumes all danish (+45)                                   |  
```  
```{=latex}  
\end{tiny}  
```  
## PR (Patient Register)    
```{=latex}  
\begin{tiny}  
```  
```md  
| Column name   | Type      | Constraints                    | Description                                            | Note                                 |  
| ------------- | --------- | ------------------------------ | ------------------------------------------------------ | ------------------------------------ |  
| UUID          | UUID      | PRIMARY KEY                    | UUID of patient                                        | Not to be confused with CPR number   |  
| NAME          | TEXT      | NOT NULL. (LENGTH(NAME) < 100) | Name of patient                                        |                                      |  
| BIRTHDATE     | DATE      | NOT NULL                       | Birthdate of patient                                   | First half of CPR number. DD/MM/YYYY |  
| CPR_KEY       | INT       | NOT NULL. 0-9999               | Last bit of the CPR number                             |                                      |  
| BIO_GENDER    | BOOL      | NOT NULL                       | The biological gender of the patient assigned at birth |                                      |  
| PRONOUNS      | TEXT      |                                | Pronouns of patient                                    |                                      |  
| CLINIC        | UUID      | FOREIGN KEY (CCR)              | UUID of main clinic associated with patient            |                                      |  
| DOCTOR        | UUID      | FOREIGN KEY (CUR)              | UUID of main doctor associated with patient            |                                      |  
| WEIGHT        | DECIMAL   | NOT NULL. WEIGHT>0             | Weight of patient                                      |                                      |  
| HEIGHT        | SMALL INT | NOT NULL. HEIGHT>0             | Height of patient                                      |                                      |  
| DIAGNOSIS     | TEXT[]    |                                | Diagnosis of patient                                   |                                      |  
| VITALS        | JSON      | NOT NULL                       | All vitals of patient                                  | This includes pulse bloodtype etc    |  
| PRESCRIPTIONS | JSON      |                                | All prescriptions of patient                           |                                      |  
| PFP           | TEXT      |                                | Path to patient pfp                                    |                                      |  
| JOURNAL       | JSON      | NOT NULL                       | Journal/Log of patient                                 |                                      |  
| APPOINTMENTS  | JSON      |                                | Appointments of patient                                |                                      |  
| LAB_RESULTS   | JSON      |                                | Lab results of patient                                 |                                      |  
```  
```{=latex}  
\end{tiny}  
```  
  
## L** (Local **)    
### LUR  
```{=latex}  
\begin{tiny}  
```  
```md  
| Column name | Type | Constraints                          | Description                             | Note                                                       |  
| ----------- | ---- | ------------------------------------ | --------------------------------------- | ---------------------------------------------------------- |  
| UUID        | UUID | PRIMARY KEY                          | UUID of user                            |                                                            |  
| EMAIL       | TEXT | NOT NULL. CHECK(LENGTH(EMAIL) < 200) | Email of user                           |                                                            |  
| PASSWORD    | TEXT | NOT NULL                             | Password of user                        | Should be hashed with argon2id                             |  
| SALT        | TEXT | NOT NULL                             | Salt for Argon2ID password hashing algo |                                                            |  
| NAME        | TEXT | NOT NULL. CHECK(LENGTH(NAME) < 1000) | Name of user                            |                                                            |  
| POSITION    | POS  | NOT NULL                             | Position of user                        | Position as enum. Position will also determin admin rights |  
| PFP         | TEXT |                                      | Profile picture of user                 | Storage path to PFP                                        |  
| CLINIC      | UUID | FOREIGN KEY                          | Clinic associated with user             |                                                            |  
| PHONE       | INT  | NOT NULL. 0-99999999                 | Phone number of user                    | Assumes all danish (+45)                                   |  
```  
```{=latex}  
\end{tiny}  
```  
  
### LPR  
```{=latex}  
\begin{tiny}  
```  
```md  
| Column name   | Type      | Constraints                    | Description                                            | Note                                 |  
| ------------- | --------- | ------------------------------ | ------------------------------------------------------ | ------------------------------------ |  
| UUID          | UUID      | PRIMARY KEY                    | UUID of patient                                        | Not to be confused with CPR number   |  
| NAME          | TEXT      | NOT NULL. (LENGTH(NAME) < 100) | Name of patient                                        |                                      |  
| BIRTHDATE     | DATE      | NOT NULL                       | Birthdate of patient                                   | First half of CPR number. DD/MM/YYYY |  
| CPR_KEY       | INT       | NOT NULL. 0-9999               | Last bit of the CPR number                             |                                      |  
| BIO_GENDER    | BOOL      | NOT NULL                       | The biological gender of the patient assigned at birth |                                      |  
| PRONOUNS      | TEXT      |                                | Pronouns of patient                                    |                                      |  
| CLINIC        | UUID      | NOT NULL                       | UUID of main clinic associated with patient            |                                      |  
| DOCTOR        | UUID      | FOREIGN KEY (LUR)              | UUID of main doctor associated with patient            |                                      |  
| WEIGHT        | DECIMAL   | NOT NULL. WEIGHT>0             | Weight of patient                                      |                                      |  
| HEIGHT        | SMALL INT | NOT NULL. HEIGHT>0             | Height of patient                                      |                                      |  
| DIAGNOSIS     | TEXT[]    |                                | Diagnosis of patient                                   |                                      |  
| VITALS        | JSON      | NOT NULL                       | All vitals of patient                                  | This includes pulse bloodtype etc    |  
| PRESCRIPTIONS | JSON      |                                | All prescriptions of patient                           |                                      |  
| PFP           | TEXT      |                                | Path to patient pfp                                    |                                      |  
| JOURNAL       | JSON      | NOT NULL                       | Journal/Log of patient                                 |                                      |  
| APPOINTMENTS  | JSON      |                                | Appointments of patient                                |                                      |  
| LAB_RESULTS   | JSON      |                                | Lab results of patient                                 |                                      |  
```  
```{=latex}  
\end{tiny}  
```
  
## Structure      
Entries follow an X.Y.Z hierarchy:      
> X: Overall Category (e.g., User Management, Patient Management).      
> Y: Feature Set (e.g., Login, Settings, Search).      
> Z: Specific Action/Endpoint (e.g., Password Reset, Entry Change).      
    
> Note: "position" field is  an integer mapping to an enum on  the database end. the  following applies:  
    1: Secretary  
    2: Nurse  
    3: Doctor  
    4: Clinic (Local) Admin  
    5: Sys Admin  
    
---    
    
# 1.y.z - User Management      
## 1.1 - Access Control      
### 1.1.1 - User Registration      
> Description: Registers a user on the system (not a patient)      
> Note: Should only be accessible by admins in Rev 3      
> Note: Implement RESTful in Rev 3      
> Endpoint: `POST /api/um/ac/register`      
> Request body:      
```json    
{    
    "email": "string",    
    "password": "string",    
    "name": "string",    
    "clinic": "string",    
    "position": "int",  
    "pfp": "image" ,  
    "phone" : "int"   
}    
```    
> Note: `password` should be hashed in Rev 3. `pfp` is optional.    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 1.1.2 - User Login      
> Description: Logs in a user      
> Endpoint: `POST /api/um/ac/login`      
> Request body:      
```json    
{    
    "email": "string",    
    "password": "string"    
}    
```    
> Note: `password` should be hashed in Rev 3. Session tokens to be introduced in Rev 3.    
    
> Exp. Response:      
`0 | success`    
    
---    
    
## 1.2 - User Deletion      
> Description: Deletes a user      
> Note: Ensure only admins have access      
> Endpoint: `DELETE /api/um/{user}/del/`      
    
> Exp. Response:      
`0 | success`    
    
---    
    
## 1.3 - User Fetching      
> Description: Fetches data on a specified user      
> Endpoint: `POST /api/um/fetch`      
> Request body:      
```json    
{    
    "email": "string"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",    
    "name": "string",    
    "clinic": "string",    
    "email": "string",    
    "position": "string",        
    "pfp": "image",  
    "phone" : "int"   
}    
```    
> Note: `pfp` is optional.    
    
---    
    
## 1.4 - User Password Reset      
> Description: Resets a user's password      
> Note: Should only be accessible by admins in Rev 3      
> Endpoint: `POST /api/um/{user}/reset`      
> Request body:      
```json    
{    
    "email": "string",    
    "new_pass": "string"    
}    
```    
> Note: `new_pass` should be hashed in Rev 3.    
    
> Exp. Response:      
`0 | success`    
    
---    
  
# 2.y.z - Patient Management      
> Note: All admins referred to in section 2 are clinic admins.    
## 2.1 - Patient Registration      
> Description: Registers a patient in the system      
> Note: Should only be accessible by admins in Rev 3      
> Endpoint: `POST /api/pm/reg`      
> Request body:      
```json    
{    
    "name": "string",    
    "pronouns": "string",    
    "clinic": "uuid", //ref to CCR    
    "bday": "date",    
    "weight": "float",    
    "bio_sex": "bool",    
    "CPR": "int",    
    "diagnoses": "[string]",    
    "vitals" : "json",  
    "prescriptions": "json",    
    "pfp": "image"    
}    
```    
> Note: `pfp` is optional.    
    
> Exp. Response:      
`0 | success`    
    
---    
    
## 2.2 - Patient Deletion      
> Description: Deletes a patient      
> Note: Ensure only admins have access      
> Endpoint: `DELETE /api/pm/{patient}/del/`      
    
> Exp. Response:      
`0 | success`    
    
---    
    
## 2.3 - Assign Patient      
### 2.3.1 - Patient Assignment info fetching      
> Description: Fetches information regarding patient and doctor(s) for (re)assignment      
> Note: Use endpoint 1.3 and 3.1.6     
    
---    
    
### 2.3.2 - Patient Assignment     
> Description: Assigns a patient to a doctor after confirmation      
> Note: Should only be accessible by admins in Rev 3      
> Endpoint: `POST /api/pm/assignPat/confd`      
> Request:      
```json    
{    
    "uuid_pt": "uuid",    
    "uuid_dr": "uuid"    
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---   
  
# 3.y.z - Doctor–Patient Interface    
## 3.1 - Fetching      
### 3.1.1 - Vitals Fetching      
> Description: Fetches all patient data excluding the journal      
> Endpoint: `POST /api/dpm/usrfet/vital`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",     
    "vitals": {    
        "date": "int",    
        //below is example data  
        "heart rate": "string",    
        "blood pressure": "string",    
        "SpO2": "string",    
    }    
}    
```    
> Note: `pfp` is optional. Update when more data fields are confirmed.    
    
---    
    
### 3.1.2 - Journal Fetching      
> Description: Fetches the patient journal      
> Endpoint: `POST /api/dpm/usrfet/journal`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",     
    "journal": {    
        "date": "int",    
        //below is example data  
        "patient_summary": "string",    
        "eprescription_edispensation": "string",    
        "laboratory_results": "string",    
        "medical_imaging_and_reports": "string",    
        "hospital_discharge_reports": "string"    
    }    
}    
```    
    
---    
    
### 3.1.3 - Prescription Fetching      
> Description: Fetches the active prescriptions for a patient      
> Endpoint: `POST /api/dpm/usrfet/prescription`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",    
    "prescriptions": "json"    
}    
```    
    
---    
    
### 3.1.4 - Diagnosis Fetching      
> Description: Fetches the diagnoses for a patient      
> Endpoint: `POST /api/dpm/usrfet/diagnosis`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",    
    "diagnoses": "[string]"    
}    
```    
    
---    
  
### 3.1.5 - Appointment Fetching      
> Description: Fetches scheduled appointments for a patient      
> Endpoint: `POST /api/dpm/usrfet/appointment`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",     
    "appointments": [    
        {    
            "appointment_id": "int",    
            "date": "date",    
            "time": "string",    
            "doctor": "uuid",  //ref to CUR  
            "notes": "string",  
            "clinic" : "uuid" //ref to CCR  
        }    
    ]    
}    
```    
    
---    
    
### 3.1.6 - Person Info Fetching      
> Description: Fetches personal/demographic information for a patient      
> Endpoint: `POST /api/dpm/usrfet/info`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",    
    "name": "string",    
    "pronouns": "string",    
    "bday": "date",    
    "bio_sex": "bool",    
    "clinic": "string",    
    "pfp": "image"    
}    
```    
> Note: `pfp` is optional.    
    
---    
  
### 3.1.7 - Lab Result Fetching      
> Description: Fetches laboratory results for a patient      
> Endpoint: `POST /api/dpm/usrfet/labresult`      
> Request:      
```json    
{    
    "CPR_pt": "int"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",     
    "lab_results": [    
        {    
            "test_issuer" : "uuid", //ref to cur  
            "test_issuer_clinic" : "uuid", //ref to ccr  
            "test_executor" : "string",       
            "test_executor_phone" : "int",        
            "result_id": "int",    
            "date": "date",    
            "test_name": "string",    
            "result": "json",    
            "unit": "string",    
            "reference_range": "string",    
            "notes": "string"    
        }    
    ]    
}    
```    
    
---    
  
## 3.2 - Updating    
### 3.2.1 - Vitals Updating      
> Description: Updates vital patient data      
> Endpoint: `POST /api/dpm/usrup/{uuid}/vital`      
> Request:      
```json    
{    
    "vitals": {    
        "date": "int",    
        //below is example data  
        "heart rate": "string",    
        "blood pressure": "string",    
        "SpO2": "string",    
    }    
}    
```    
> Note: `pfp` is optional. Update when more data fields are confirmed.    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 3.2.2 - Journal Updating      
> Description: Updates the patient journal      
> Endpoint: `POST /api/dpm/usrup/{uuid}/journal`      
> Request:      
```json    
{    
    "journal": {    
        "date": "int",    
        //below is example data  
        "patient_summary": "string",    
        "eprescription_edispensation": "string",    
        "laboratory_results": "string",    
        "medical_imaging_and_reports": "string",    
        "hospital_discharge_reports": "string"    
    }    
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 3.2.3 - Prescription Updating      
> Description: Updates the active prescriptions for a patient      
> Endpoint: `POST /api/dpm/usrup/{uuid}/prescription`      
> Request:      
```json    
{    
    "prescriptions": "json"    
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 3.2.4 - Diagnosis Updating      
> Description: Updates the diagnoses for a patient      
> Endpoint: `POST /api/dpm/usrup/{uuid}/diagnosis`      
> Request:      
```json    
{    
    "diagnoses": "[string]"    
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 3.2.5 - Appointment Updating      
> Description: Updates a scheduled appointment for a patient      
> Endpoint: `POST /api/dpm/usrup/{uuid}/appointment`      
> Request:      
```json    
{     
    "appointment": {    
        "appointment_id": "uuid",    
        "date": "date",    
        "time": "string",    
        "doctor": "uuid",  //ref to CUR  
        "clinic" : "uuid", //ref to CCR  
        "notes": "string"    
    }    
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 3.2.6 - Person Info Updating      
> Description: Updates personal/demographic information for a patient      
> Endpoint: `POST /api/dpm/usrup/{uuid}/info`      
> Request:      
```json    
{    
    "cpr_key": "int",    
    "name": "string",    
    "pronouns": "string",    
    "bday": "date",    
    "bio_sex": "bool",    
    "pfp": "image"    
}    
```    
> Note: `pfp` is optional.    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 3.2.7 - Lab Result Updating      
> Description: Adds or updates a laboratory result for a patient      
> Endpoint: `POST /api/dpm/usrup/{uuid}/labresult`      
> Request:      
```json    
{    
    "lab_result": {    
        "test_issuer" : "uuid", //ref to cur      
        "test_issuer_clinic" : "uuid", //ref to ccr  
        "test_executor" : "string",  
        "test_executor_phone" : "int",  
        "result_id": "int",    
        "date": "date",    
        "test_name": "string",    
        "result": "string",    
        "unit": "string",    
        "reference_range": "string",    
        "notes": "string"    
    }    
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---    

## 3.3 - Patient overview
\> Description: Fetches all patients for a given doctor
\> Endpoint: `POST /api/dpm/pf/{doctor_uuid}`
\> Exp.Response:
```json
{
    "pat1" : {
        "name" : "string",
        "pronouns" : "string",
        "age" : "int",
        "pfp" : "string" //path to pfp
    },
    "pat2" : {
        "name" : "string",
        "pronouns" : "string",
        "age" : "int",
        "pfp" : "string" //path to pfp
    },
    {...},
    "patn" : {
        "name" : "string",
        "pronouns" : "string",
        "age" : "int",
        "pfp" : "string" //path to pfp
    }
}
```

## 3.4 - Calendar
### 3.4.1 - Calendar fetching
\> Description: Fetches all apointments for given doctor
\> Endpoint: `POST /api/dpm/calendar/sync/{uuid}` //dr
\> Exp. Response:
```json
{
    "apt1" : {
        "name" : "string",
        "reason" : "string",
        "time" : "int", //unix time
        "pfp" : "string" //path to pfp
    },
    "apt2" : {
        "name" : "string",
        "reason" : "string",
        "time" : "int", //unix time
        "pfp" : "string" //path to pfp
    },
    {...},
    "aptn" : {
        "name" : "string",
        "reason" : "string",
        "time" : "int", //unix time
        "pfp" : "string" //path to pfp
    },
}
```
### 3.4.2 - Appointment creation
\> Description: Creates a new appointment
\> Endpoint: `POST /api/dpm/calendar/create/{uuid}` //pt
\> Request:
```json
{
    "pt. name" : "string",
    "reason for apt." : "string",
    "time" : "int",
    "pfp" : "string"
}
```
> Exp. Response:
0 | Success

## 3.5 - permission management
### 3.5.1 - Permission updating
\> Description: Permissions for foreign doctors
\> Endpoint: `POST /api/dpm/perm/{uuid}` //pt
\> Request:
```json
{
    "dr.1" : {
        "dr. uuid" : "int",
        "perm int" : "int" //each bit in the integer will be treated as a bool
    },
    "dr.2" : {
        "dr. uuid" : "int",
        "perm int" : "int" //each bit in the integer will be treated as a bool
    },
    {...},
    "dr.n" : {
        "dr. uuid" : "int",
        "perm int" : "int" //each bit in the integer will be treated as a bool
    },
}
```
> Exp. Response:
0 | Success

### 3.5.2 - Permission fetching
\> Description: Permissions for foreign doctors
\> Endpoint: `POST /api/dpm/perm/{uuid}` //pt
\> Exp. Response:
```json
{
    "dr.1" : {
        "dr. uuid" : "int",
        "perm int" : "int" //each bit in the integer will be treated as a bool
    },
    "dr.2" : {
        "dr. uuid" : "int",
        "perm int" : "int" //each bit in the integer will be treated as a bool
    },
    {...},
    "dr.n" : {
        "dr. uuid" : "int",
        "perm int" : "int" //each bit in the integer will be treated as a bool
    },
}
```

## 3.6 - Doctor timeline
\> Description: Timeline of da doctor
\> Endpoint: `POST /api/dpm/{uuid}/timeline` //pt
\> Exp. Response:
```json
{
    "journal": {    
        "date": "int",    
        //below is example data  
        "patient": "string",    
        "doctor_accessing": "string",    
        "data_type": "string",    
        "changes": "string",
        "severity" : "int"    
    }  
}
```


# 4.y.z - Sysadmin      
> Note: For security reasons, sysadmins should only be creatable via CLI.      
## 4.1 - Clinic Management      
### 4.1.1 - Create Clinic      
> Description: Creates a new clinic in the CCR      
> Endpoint: `POST /api/sudo/cc`      
> Request:      
```json    
{    
    "name": "string",    
    "location": "string",    
    "email": "string",  //optional  
    "phone": "int",  
    "cvr" : "int"  
}    
```    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 4.1.2 - Fetch Clinic      
> Description: Fetches a clinic from the CCR      
> Endpoint: `POST /api/sudo/fc`      
> Request:      
```json    
{    
    "email": "string"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "name": "string",    
    "uuid": "string",    
    "location": "string",    
    "email": "string",    
    "phone": "int",  
    "cvr" : "int"  
}    
```    
    
---    
    
### 4.1.3 - Delete Clinic      
\> Description: Deletes a clinic from the CCR      
\> Endpoint: `DELETE /api/sudo/dc/{uuid}`      
    
> Exp. Response:      
`0 | success`    
    
---    
    
## 4.2 - Local Admin Management      
### 4.2.1 - Create Local Admin      
> Description: Registers a local admin on the system      
> Note: Should only be accessible by sysadmins in Rev 3      
> Endpoint: `POST /api/sudo/lam/create`      
> Request body:      
```json    
{    
    "email": "string",    
    "password": "string",    
    "name": "string",    
    "clinic": "string",    
    "pfp": "image",  
    "phone" : "int",  
    "position" : "int" //always 4, see top comment    
}    
```    
> Note: `password` should be hashed in Rev 3. `pfp` is optional.    
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 4.2.2 - Delete Local Admin      
> Description: Deletes a local admin      
> Note: Ensure only sysadmins have access      
> Endpoint: `DELETE /api/sudo/lam/{user}/del/`      
    
> Exp. Response:      
`0 | success`    
    
---    
    
### 4.2.3 - Fetch Local Admin      
> Description: Fetches a local admin from the system      
> Note: Should only be accessible by sysadmins in Rev 3      
> Endpoint: `POST /api/sudo/lam/fetch`      
> Request body:      
```json    
{    
    "email": "string"    
}    
```    
    
> Exp. Response:      
```json    
{    
    "uuid": "int",    
    "email": "string",    
    "name": "string",    
    "clinic": "string",    
    "pfp": "image",  
    "phone" : "int"  
}    
```    
> Note: `pfp` is optional.    
    
---    
    
# Error Codes      
Errors are categorised as X.YY, where X is the category and YY is the error number.    
    
> 0 — Success    
    
> 1.YY — Application / system error    
    
    1.01 — Communication with backend lost    
    1.02 — Backend error    
    1.03 — Database error    
    1.04 — Patient already exists    
    1.05 — Patient does not exist    
    1.06 — Patient journal does not exist    
    1.07 — Database timeout    
    1.08 — Database write failure    
    1.09 — Database read failure    
    1.10 — Service unavailable    
    1.11 — Internal server error    
    1.12 — Dependent service failure (e.g. L** sync failure)    
    1.13 — File upload failure    
    1.14 — File too large    
    1.15 — Unsupported file type    
    
    
> 2.YY — User / validation error    
    
    2.01 — Invalid credentials    
    2.02 — User already registered    
    2.03 — Clinic does not exist    
    2.04 — User does not exist    
    2.05 — Missing required field    
    2.06 — Invalid field type or format    
    2.07 — Invalid CPR number    
    2.08 — Invalid email format    
    2.09 — Password does not meet requirements    
    2.10 — Date of birth invalid or out of range    
    2.11 — Patient already assigned to doctor    
    2.12 — Doctor does not belong to specified clinic    
  
> 3.YY — Connection / infrastructure error    
    
    3.01 — Request timeout    
    3.02 — L** node unreachable    
    3.03 — C** sync failure    
    3.04 — Network error    
    3.05 — DNS resolution failure    
    
    
> 4.YY — Security / authorisation error    
    
    4.01 — Unauthorised (no credentials provided)    
    4.02 — Forbidden (insufficient permissions)    
    4.03 — Session expired    
    4.04 — Account locked    
    4.05 — Account suspended    
    4.06 — Too many failed login attempts    
    4.07 — Action requires admin privileges    
    4.08 — Cross-clinic access violation    
    
    
> 7.YY — Miscellaneous error    
    
    7.01 — UUID already exists    
    7.02 — Generic registration error    
    7.03 — Unknown error    
    7.04 — Not implemented