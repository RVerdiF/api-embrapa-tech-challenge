from pydantic import BaseModel, Field, field_validator
from typing import Optional

class Mesa(BaseModel):
    index: Optional[int] = Field(default=None)
    pais: str = Field(...)
    produto: str = Field(...)
    quantidade: float = Field(...)
    ano: int = Field(...)

    class Config:
        from_attributes = True  # Allows model to work with ORMs
        validate_assignment = True  # Validates assignments to model fields
        str_strip_whitespace = True  # Strips whitespace from string values

    @field_validator('ano')
    def validate_ano(cls, v):
        if v < 1900 or v > 2100:  # reasonable year range
            raise ValueError('Year must be between 1900 and 2100')
        return v

    @field_validator('quantidade')
    def validate_quantidade(cls, v):
        if v < 0:
            raise ValueError('Quantidade must be non-negative')
        return v

class Espumantes(BaseModel):
    index: Optional[int] = Field(default=None)
    pais: str = Field(...)
    produto: str = Field(...)
    quantidade: float = Field(...)
    ano: int = Field(...)

    class Config:
        from_attributes = True  # Allows model to work with ORMs
        validate_assignment = True  # Validates assignments to model fields
        str_strip_whitespace = True  # Strips whitespace from string values

    @field_validator('ano')
    def validate_ano(cls, v):
        if v < 1900 or v > 2100:  # reasonable year range
            raise ValueError('Year must be between 1900 and 2100')
        return v

    @field_validator('quantidade')
    def validate_quantidade(cls, v):
        if v < 0:
            raise ValueError('Quantidade must be non-negative')
        return v

class Frescas(BaseModel):
    index: Optional[int] = Field(default=None)
    pais: str = Field(...)
    produto: str = Field(...)
    quantidade: float = Field(...)
    ano: int = Field(...)

    class Config:
        from_attributes = True  # Allows model to work with ORMs
        validate_assignment = True  # Validates assignments to model fields
        str_strip_whitespace = True  # Strips whitespace from string values

    @field_validator('ano')
    def validate_ano(cls, v):
        if v < 1900 or v > 2100:  # reasonable year range
            raise ValueError('Year must be between 1900 and 2100')
        return v

    @field_validator('quantidade')
    def validate_quantidade(cls, v):
        if v < 0:
            raise ValueError('Quantidade must be non-negative')
        return v

class Sucos(BaseModel):
    index: Optional[int] = Field(default=None)
    pais: str = Field(...)
    produto: str = Field(...)
    quantidade: float = Field(...)
    ano: int = Field(...)

    class Config:
        from_attributes = True  # Allows model to work with ORMs
        validate_assignment = True  # Validates assignments to model fields
        str_strip_whitespace = True  # Strips whitespace from string values

    @field_validator('ano')
    def validate_ano(cls, v):
        if v < 1900 or v > 2100:  # reasonable year range
            raise ValueError('Year must be between 1900 and 2100')
        return v

    @field_validator('quantidade')
    def validate_quantidade(cls, v):
        if v < 0:
            raise ValueError('Quantidade must be non-negative')
        return v
    
class Passas(BaseModel):
    index: Optional[int] = Field(default=None)
    pais: str = Field(...)
    produto: str = Field(...)
    quantidade: float = Field(...)
    ano: int = Field(...)

    class Config:
        from_attributes = True  # Allows model to work with ORMs
        validate_assignment = True  # Validates assignments to model fields
        str_strip_whitespace = True  # Strips whitespace from string values

    @field_validator('ano')
    def validate_ano(cls, v):
        if v < 1900 or v > 2100:  # reasonable year range
            raise ValueError('Year must be between 1900 and 2100')
        return v

    @field_validator('quantidade')
    def validate_quantidade(cls, v):
        if v < 0:
            raise ValueError('Quantidade must be non-negative')
        return v