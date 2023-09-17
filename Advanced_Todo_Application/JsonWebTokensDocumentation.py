# Json Web Tokens (JWT) Overview

# What is a Json Web Token ?

# JSON Web Token is a self-contained way to securely transmit the information
# and data between two parties using a JSON Object.

# JSON Web Tokens can be trusted because each JWT can be digitally signed,
# which in return allows the server to know if the JWT has been changed at all.

# JWT should be used while handling authorization.

# JWT is a great way for information to be exchanged between the server and client.

# JSON Web Token Structure

# A JSON Web Token is created of three seperate parts which are seperated by dots (.)
# The parts of the JSON Web Token are as below:
# 1. Header (a)
# 2. Payload (b)
# 3. Signature (c)

# JSON Web Token: aaaaaaaa.bbbbbbbb.cccccccc

# ---------------------------------------------------- #
# JWT Header:
# A JWT header usually consists of two parts:
# "alg" The algorithm for signing
# "typ" The specific type of token

# The JWT header is then encoded using Base64
# to create the first part of the JWT (a).

# An example of JWT Header:
# {
# "alg": "HS256",
# "typ": "JWT"
# }
# --------------------------------------------------------------
# JWT Payload
# A JWT Payload consists of the data. The Payloads data
# contains claims, and there are three different types
# of claims.
# Types of Claims:
# 1-) Registered: They are the claims that are pre-defined.
# The top three registered claims include iss, sub, and exp.
# "iss" stands for the issuer. This claim identifies the
# principal that issued the JWT. Sub stands for the subject
# and it holds statements about the subject. The subject value
# must be scoped either locally or globally unique. We can
# think of a subject as an ID for the Json Web Token. Exp stands
# for the expiration time, which is when the JWT expires. The
# "Exp" claim makes sure that the current date and time are
# before the expiration date and time of the token.

# We should make sure that an expiration date is attached to each JWT
# for preventing potentially unauthorized logins.

# 2-) Private
# 3-) Public

# The JWT Payload is then encoded using Base64
# to create the second part of the JWT.

# --------------------------------------------------------------
# JWT Signature
# A JWT Signature is created by using the algorith
# in the hader to hash out the encoded header, encoded
# payload with a secret.

# The secret can be anything, but is saved somewhere on
# the server which the client does not have access to.

# The signature is the third and final part of a JWT (c).
# aaaaaaaa.bbbbbbbb.cccccccc
# --------------------------------------------------------------

# Note: The JWT is safe as long as the client does not find
# out the secret key.

# Using JWT is extremely popular in modern software architectures
# like microservices, where each API might be loosely coupled.
