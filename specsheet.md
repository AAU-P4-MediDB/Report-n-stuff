> MediDB Specsheet revision 1  
> by @voxvoltera & @lilleole  
> latest update: 10/03/2026  

# Revision notes  
This is the earliest revision of the specsheet, containing only confirmed known features as per 10/03/2026, such as login, chat functionality, and more  
Revision 2 will contain the finalised application layout, and Revision 3 will finally add the security layers  

# Purpose  
The purpose of this document is to be the singular source of truth for both frontend and backend development. It aims to prevent either team from blocking one another, or having to wait for a certain feature to be implmented before they can staert their work  
Any deviation from this document should only happen after consulting with any of the document maintainers, and subsequent updating of the specifications  

# Usage  
This specsheet is to be viewed as a reference manuial rather than a todo list.  
Implementation order is dictated by the Kanban board, and the order in which tickets are listed. Each Kanban ticket will map to a specific entry in this specsheet (eg. [2.4.7]) to ensure the implementation matches the design, and is carried out in the correct order in accordance to testing efforts  

# Database  
write stuff  

## Structure  
Entries follow a X.Y.Z hierarchy:  
> X: Overall Category (e.g., User Management, Patient Management).  
> Y: Feature Set (e.g., Login, Settings, Search).  
> Z: Specific Action/Endpoint (e.g., Password Reset, Entry Change).  

# 1.y.z - User Management  
## 1.1 - Access control  
### 1.1.1 - User Registration  
> Description: Registers a user on the system (not a patient)  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/um/ac/register`  
> Request body:  
```json 
{
    "email": "string",
    "password": "string", //should be hashed in rev 3
    "name": "string",
    "clinic": "string",
    "position": "string",
    "pfp": "image" [optional]
}
``` 
> Exp. Response:  
0 | success  

### 1.1.2 - User login  
> Description: Logs in a user  
> Endpoint: `/api/um/ac/login`  
> Request body:  
```json
{
    "email" : "string",
    "password" : "string", //should be hashed in rev 3
}
```

> Exp. Response:  
0 | success  

### 1.1.3 - User Password Reset  
> Description: Resets a users password  
> Endpoint: `/api/um/ac/reset`  
> Note: // should only be accessible by admin in Rev 3  
> Request body:  
```json
{
    "email" : "string",
    "new_pass" : "string" //should be hashed in rev 3
}
```
> Exp. Response:  
0 | success  

## 1.2 - User deletion  
### 1.2.1 - User deletion pre confirmation  
> Description: fetches data on specified user, and awaits admin confirmation  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/um/del/pre`  
> Request body:  
```json
{
    "email" : "string"
}
```

> Exp. Response:  
```json
{
    "uuid" : "int",
    "name" : "string",
    "clinic": "string",
    "email" : "string",
    "position": "string",
    "pfp": "image" [optional]
}
```

### 1.2.2 - User deletion post confirmation  
> Description: Deletes a user after positive confirmation in 1.2.1  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/um/del/confd`  
> Request body:  
```json
{
    "uuid" : "int"
}
```

> Exp. Response:  
0 | success  

# 2.y.z - Admin Patient management  
## 2.1 - Patient registration  
> Description: Registers a patient in the system  
> Note:// should only be accessible by admin in Rev 3  
> Endpoint: `/api/APM/reg`  
> Request body:  
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
    "pfp": "image" [optional]
}
```

> Exp. Response:  
0 | success  

# 2.2 - Patient deletion  
### 2.2.1 - User deletion pre confirmation  
> Description: fetches data on specified user, and awaits admin confirmation  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/APM/del/pre`  
> Request body:  
```json
{
    "cpr" : "int"
}
```

> Exp. Response:  
```json
{
    "uuid" : "int",
    "name" : "string",
    "clinic" : "string",
    "pronouns":"string",
    "b-day":"date",
    "weight":"float",
    "pfp": "image" [optional]
}
```

### 2.2.2 - Patient deletion post confirmation  
> Description: Deletes a patient after positive confirmation in 2.2.1  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/APM/del/confd`  
> Request body:  
```json
{
    "uuid" : "int"
}
```

> Exp. Response:  
0 | success  

## 2.3 - Assign patient  
### 2.3.1 - Patient assignment pre confirmation  
> Description: Fetches information regarding patient and doctor(s) for (re)assignment  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/APM/assignPat/preconfd`  
> Request:  
```json
{
    "CPR_pt" : "int",
    "email_dr" : "string"
}
```

> Exp. Response:  
```json
{
    "Patient" : {
        "uuid" : "int",
        "name" : "string",
        "pronouns":"string",
        "clinic" : "string",
        "b-day":"date",
        "weight":"float",
        "pfp": "image" [optional]
    },
    "Doctor" : {
        "uuid" : "int",
        "name" : "string",
        "clinic": "string",
        "email" : "string",
        "position": "string",
        "pfp": "image" [optional]
    },
    "Doctor2" : { //optional
        "uuid" : "int",
        "name" : "string",
        "clinic": "string",
        "email" : "string",
        "position": "string",
        "pfp": "image" [optional]
    }
}
```

### 2.3.2 - Patient assignment post confirmation  
> Description: Assigns patient doctor after confirmation  
> Note: // should only be accessible by admin in Rev 3  
> Endpoint: `/api/APM/assignPat/confd`  
> Request:  
```json
{
    "uuid_pt" : "int",
    "uuid_dr" : "int"
}
```

> Exp. Response:  
0 | success  

# 3.y.z - Doctor Patient management  
## 3.1 - User fetching  
### 3.1.1 - Vitals  
> Description: Fetches everything about a patient minus the journal  
> Endpoint: `/api/dpm/usrfet/vital`  
> Request:  
```json
{
    "CPR_pt" : "int"
}
```

> Exp. Response:  
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
    "pfp": "image" [optional]
    // UPDATE WHEN MORE DATA ARIVES
}
```

### 3.1.2 - Journal  
> Description: Fetches patient journal  
> Endpoint: `/api/dpm/usrfet/journal`  
> Request:  
```json
{
    "CPR_pt" : "int"
}
```

> Exp. Response:  
```json
{
    "uuid" : "int",
    "cpr" : "int",
    "journal" : {
        //do later
    }
}
```

## 3.2 - User updating  
### 3.2.1 - Vitals  
> Description: Fetches everything about a patient minus the journal  
> Endpoint: `/api/dpm/usrup/vital`  
> Request:  
```json
{
    "uuid" : "int",
    "weight":"float",
    "diagnosees" : "[string]",
    "prescriptions" : "json",
    "pfp": "image" [optional]
    // UPDATE WHEN MORE DATA ARIVES
}
```

> Exp. Response:  
0 | success  

### 3.2.2 - Journal  
> Description: Fetches patient journal  
> Endpoint: `/api/dpm/usrup/journal`  
> Request:  
```json
{
    "uuid" : "int",
    "cpr" : "int",
    "journal" : {
        //do later
    }
}
```

> Exp. Response:  
0 | success  

# 4.y.z - Supreme Admin
//rev2

# Error codes  
errors are categorised on x.yy, where x is the category and yy is the error number  
> 0 - success  
> 1.yy - application/system error  
- 1 - communication with backend lost  
- 2 - Backend error  
- 3 - Database error  
- 4 - Patient already exists  
- 5 - Patient doesn't exists  
- 6 - Patient journal does not exist  
  
> 2.yy - User/validation error  
- 1 - Invalid credentials  
- 2 - User already registered  
- 3 - clinic doesn't exist  
- 4 - User doesn't exist //deletion  
  
> 3.yy - connection/infrastructure error  
  
> 4.yy - security/authorisation error  
  
> 7.yy - misc. error  
- 1 - UUID already exists  
- 2 - Generic registration error  

> 2.yy - User/validation error
- 1 - Invalid credentials
- 2 - User already registered
- 3 - clinic doesn't exist
- 4 - User doesn't exist //deletion

> 3.yy - connection/infrastructure error

> 4.yy - security/authorisation error

> 7.yy - misc. error
- 1 - UUID already exists
- 2 - Generic registration error
