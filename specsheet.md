> MediDB Specsheet revision 1
> by @voxvoltera & @lilleole
> latest update: 27/02/2026 @ 13:37

# Revision notes
This is the earliest revision of the specsheet, containing only confirmed known features as per 10/03/2026, such as login, chat functionality, and more
Revision 2 will contain the finalised application layout, and Revision 3 will finally add the security layers

# Purpose
The purpose of this document is to be the singular source of truth for both frontend and backend development. It aims to prevent either team from blocking one another, or having to wait for a certain feature to be implmented before they can staert their work
Any deviation from this document should only happen after consulting with any of the document maintainers, and subsequent updating of the specifications

# Usage
This specsheet is to be viewed as a reference manuial rather than a todo list.
Implementation order is dictated by the Kanban board, and the order in which tickets are listed. Each Kanban ticket will map to a specific entry in this specsheet (eg. [2.4.7]) to ensure the implementation matches the design, and is carried out in the correct order in accordance to testing efforts

## Structure
Entries follow a X.Y.Z hierarchy:

> X: Overall Category (e.g., User Management, Patient Management).

> Y: Feature Set (e.g., Login, Settings, Search).

> Z: Specific Action/Endpoint (e.g., Password Reset, Entry Change).

# 1.y.z - User Management

# 2.y.z - Admin

# 3.y.z - Patient management



# Error codes
errors are categorised on x.yy, where x is the category and yy is the error number

> 0.yy - application/system error
> 1.yy - User/validation error
> 2.yy - connection/infrastructure error
> 3.yy - security/authorisation error
> 6.yy - misc. error
