\> MediDB Specsheet revision 1.1
\> by @voxvoltera & @lilleole  
\> latest update: 14/03/2026  

# Revision notes  
Revised architecture for centralised server layout, and corrected minor mistakes... see diff for changes

# Purpose  
The purpose of this document is to be the singular source of truth for both frontend and backend development. 
It aims to prevent either team from blocking one another, or having to wait for a certain feature to be implmented before they can start their work  
Any deviation from this document should only happen after consulting with any of the document maintainers, and subsequent updating of the specifications  

# Usage  
This specsheet is to be viewed as a reference manuial rather than a todo list.  
Implementation order is dictated by the Kanban board, and the order in which tickets are listed. Each Kanban ticket will map to a specific entry in this specsheet (eg. [2.4.7]) to ensure the implementation matches the design, and is carried out in the correct order in accordance to testing efforts  

# Database  
## CCR (Central Clinic Register)
\> Description: contains information about a clinic such as doctors, admins, patient count and cpr, etc.

## CUR (Central User Register)
\> Description: Contains information about users login information, their relation to CCR, etc.

## CPR (Central Patient Register)
\> Description: Contains all information about all patients, and their relation to CCR

## L** (Local * *)
\> Description: Local, clinic specific, copies of the C** databases, to ensure high availability even in the case of fatal infrastructure failure

## Structure  
Entries follow a X.Y.Z hierarchy:  
\> X: Overall Category (e.g., User Management, Patient Management).  
\> Y: Feature Set (e.g., Login, Settings, Search).  
\> Z: Specific Action/Endpoint (e.g., Password Reset, Entry Change).  

\> Note: There are 2 categories of admins. Sysadmins who administrate the centralised servers, and clinic  admins who administrate the local clinic.if there's just refered to "admins" it's either of the above

# 1.y.z - User Management  
## 1.1 - Access control  
### 1.1.1 - User Registration  
\> Description: Registers a user on the system (not a patient)  
\> Note:  should only be accessible by admins in Rev 3  
\> Note: Implement RESTfull in rev 3
\> Endpoint: `/api/um/ac/register`  
\> Request body:  
```json 
{
    "email": "string",
    "password": "string", //should be hashed in rev 3
    "name": "string",
    "clinic": "string",
    "position": "string",
    "admin" : "bool",
    "pfp": "image" //[optional]    
}
``` 
\> Exp. Response:  
0 | success  

### 1.1.2 - User login  
\> Description: Logs in a user  
\> Endpoint: `/api/um/ac/login`  
\> Request body:  
```json
{
    "email" : "string",
    "password" : "string", //should be hashed in rev 3
}
```

\> Exp. Response:  
0 | success  session tokens in rev3

## 1.2 - User deletion
\> Description: Deletes a user
\> Note: ensure only  admins  have  access
\> Endpoint: `/api/um/{user}/del/`  
\> Exp. Response:  
0 | success  

## 1.3 - User fetching
\> Description: fetches data on specified user
\> Endpoint: `/api/um/fetch`  
\> Request body:  
```json
{
    "email" : "string"
}
```

\> Exp. Response:  
```json
{
    "uuid" : "int",
    "name" : "string",
    "clinic": "string",
    "email" : "string",
    "position": "string",
    "admin" : "bool",
    "pfp": "image" //[optional]
}
```

### 1.4 - User Password Reset  
\> Description: Resets a users password  
\> Endpoint: `/api/um/{user}/reset`  
\> Note:  should only be accessible by admin in Rev 3  
\> Request body:  
```json
{
    "email" : "string",
    "new_pass" : "string" //should be hashed in rev 3
}
```
\> Exp. Response:  
0 | success  

# 2.y.z - Patient management  
\> Note: All admins refered to in section 2 are clinic admins
## 2.1 - Patient registration  
\> Description: Registers a patient in the system  
\> Note: should only be accessible by admin in Rev 3  
\> Endpoint: `/api/pm/reg`  
\> Request body:  
```json
{
    "name":"string",
    "pronouns":"string",
    "clinic" : "string",
    "b-day":"date",
    "weight":"float",
    "bio-sex":"bool",
    "CPR":"int",
    "diagnosees" : "[string]",
    "blood type" : "int",
    "prescriptions" : "json",
    "pfp": "image" //[optional]
}
```

\> Exp. Response:  
0 | success  

## 2.2 - Patient deletion
\> Description: Deletes a patient
\> Note: ensure only  admins  have  access
\> Endpoint: `/api/pm/{patient}/del/`  
\> Exp. Response:  
0 | success  

## 2.3 - User fetching
\> Description: fetches data on specified user
\> Endpoint: `/api/pm/fetch`  
\> Request body:  
```json
{
    "email" : "string"
}
```

\> Exp. Response:  
```json
{
    "uuid" : "int",
    "name" : "string",
    "clinic": "string",
    "email" : "string",
    "position": "string",
    "admin" : "bool",
    "pfp": "image" //[optional]
}
```

## 2.4 - Assign patient  
### 2.4.1 - Patient assignment pre confirmation  
\> Description: Fetches information regarding patient and doctor(s) for (re)assignment  
\> Note:  should only be accessible by admin in Rev 3  
\> Endpoint: `/api/pm/assignPat/preconfd`  
\> Request:  
```json
{
    "CPR_pt" : "int",
    "email_dr" : "string"
}
```

\> Exp. Response:  
```json
{
    "Patient" : {
        "uuid" : "int",
        "name" : "string",
        "pronouns":"string",
        "clinic" : "string",
        "b-day":"date",
        "weight":"float",
        "pfp": "image" //[optional]
    },
    "Doctor" : {
        "uuid" : "int",
        "name" : "string",
        "clinic": "string",
        "email" : "string",
        "position": "string",
        "pfp": "image" //[optional]
    },
    "Doctor2" : { //optional - only to be used during reassignments
        "uuid" : "int",
        "name" : "string",
        "clinic": "string",
        "email" : "string",
        "position": "string",
        "pfp": "image" //[optional]
    }
}
```

### 2.4.2 - Patient assignment post confirmation  
\> Description: Assigns patient doctor after confirmation  
\> Note:  should only be accessible by admin in Rev 3  
\> Endpoint: `/api/pm/assignPat/confd`  
\> Request:  
```json
{
    "uuid_pt" : "int",
    "uuid_dr" : "int"
}
```

\> Exp. Response:  
0 | success  

## 2.5 - Patient fetching  
### 2.5.1 - Vitals  
\> Description: Fetches everything about a patient minus the journal  
\> Endpoint: `/api/dpm/usrfet/vital`  
\> Request:  
```json
{
    "CPR_pt" : "int"
}
```

\> Exp. Response:  
```json
{
    "uuid":"int",
    "name":"string",
    "pronouns":"string",
    "clinic" : "string",
    "b-day":"date",
    "weight":"float",
    "bio-sex":"bool",
    "CPR":"int",
    "diagnosees" : "[string]",
    "blood type" : "int",
    "prescriptions" : "json",
    "pfp": "image" //[optional]
     //UPDATE WHEN MORE DATA ARIVES
}
```

### 2.5.2 - Journal  
\> Description: Fetches patient journal  
\> Endpoint: `/api/dpm/usrfet/journal`  
\> Request:  
```json
{
    "CPR_pt" : "int"
}
```

\> Exp. Response:  
```json
{
    "uuid" : "int",
    "cpr" : "int",
    "journal" : {
        //do later
    }
}
```

## 2.6 - Patient updating  
### 2.6.1 - Vitals  
\> Description: Fetches everything about a patient minus the journal  
\> Endpoint: `/api/dpm/usrup/vital`  
\> Request:  
```json
{
    "uuid" : "int",
    "weight":"float",
    "diagnosees" : "[string]",
    "prescriptions" : "json",
    "pfp": "image" //[optional]
     //UPDATE WHEN MORE DATA ARIVES
}
```

\> Exp. Response:  
0 | success  

### 2.6.2 - Journal  
\> Description: Fetches patient journal  
\> Endpoint: `/api/dpm/usrup/journal`  
\> Request:  
```json
{
    "uuid" : "int",
    "cpr" : "int",
    "journal" : {
        //do later
    }
}
```

\> Exp. Response:  
0 | success  

# 4.y.z - Sysadmins
\> Note: For security reasons, sysadmins should only be creatable via cli

## 4.1 - Create clinic
\> Description: Creates a new clinic in the CCR
\> Endpoint: `/api/sudo/cc`  
\> Request:  
```json
{
    "Name" : "string",
    "Location" : "string",
    "email" : "string",
    "phone" : "int",
    "Doctor count" : "int",
    "Adm count" : "int",
    "patient count" : "int",
}
```

\> Exp. Response:  
0 | success 

## 4.2 - Local Admin Management
### 4.2.1 - Create local admin
\> Description: Registers a local admin on the system
\> Note:  should only be accessible by admins in Rev 3  
\> Endpoint: `/api/sudo/lam/create`  
\> Request body:  
```json 
{
    "email": "string",
    "password": "string", //should be hashed in rev 3
    "name": "string",
    "clinic": "string",
    "pfp": "image" //[optional]    
}
``` 
\> Exp. Response:  
0 | success  


### 4.2.2 - reassign local admin pre conf
\> Description: Fetches information regarding the local admin,  and reassigns after conf
\> Note:  should only be accessible by admin in Rev 3  
\> Endpoint: `/api/sudo/lam/assign_pre`  
\> Request:  
```json
{
    "Clinic_email" : "string",
    "Local Admin email" : "string"
}
```

\> Exp. Response:  
```json
{
    "Local admin" : {
        "email": "string",
        "password": "string", //should be hashed in rev 3
        "name": "string",
        "clinic": "string",
        "uuid" : "int",
        "pfp": "image" //[optional]   
    },
    "Clinic.old" : {
        "Name" : "string",
        "Location" : "string",
        "email" : "string",
        "phone" : "int",
        "Doctor count" : "int",
        "Adm count" : "int",
        "patient count" : "int",
        "uuid" : "int"
    },
    "Clinic.new" : {
        "Name" : "string",
        "Location" : "string",
        "email" : "string",
        "phone" : "int",
        "Doctor count" : "int",
        "Adm count" : "int",
        "patient count" : "int",
        "uuid" : "int"
    }
}
```

### 4.2.3 - Patient assignment post confirmation  
\> Description: Assigns patient doctor after confirmation  
\> Note:  should only be accessible by admin in Rev 3  
\> Endpoint: `/api/pm/assignPat/confd`  
\> Request:  
```json
{
    "uuid_la" : "int",
    "uuid_newClinic" : "int"
}
```

\> Exp. Response:  
0 | success  

### 4.2.4 - delete local admin
\> Description: Deletes a local admin
\> Note: ensure only  admins  have  access
\> Endpoint: `/api/sudo/lam/{user}/del/`  
\> Exp. Response:  
0 | success  

### 4.2.4 -  LA fetching
\> Description: Fetches a local admin on the system
\> Note:  should only be accessible by admins in Rev 3  
\> Endpoint: `/api/sudo/lam/fetch`  
\> Request body:  
```json 
{
    "email": "string",   
}
``` 
\> Exp. Response:  
```json 
{
    "email": "string",
    "password": "string", //should be hashed in rev 3
    "name": "string",
    "clinic": "string",
    "uuid" : "int",
    "pfp": "image" //[optional]    
}
``` 

# Error codes  
errors are categorised on x.yy, where x is the category and yy is the error number  

\> 0 - success  

\> 1.yy - application/system error  
- 1 - communication with backend lost  
- 2 - Backend error  
- 3 - Database error  
- 4 - Patient already exists  
- 5 - Patient doesn't exists  
- 6 - Patient journal does not exist  
  
\> 2.yy - User/validation error  
- 1 - Invalid credentials  
- 2 - User already registered  
- 3 - clinic doesn't exist  
- 4 - User doesn't exist deletion  
  
\> 3.yy - connection/infrastructure error  
  
\> 4.yy - security/authorisation error  
  
\> 7.yy - misc. error  
- 1 - UUID already exists  
- 2 - Generic registration error  
