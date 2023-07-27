import uuid
from sqlalchemy import Column, String, Text, FLOAT, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from db import Base


# -------------Model-------------

class Menu(Base):
    __tablename__ = 'menus'

    target_menus_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    target_menus_title = Column(String(50), unique=True)
    target_menus_description = Column(Text)


class Submenu(Base):
    __tablename__ = 'submenus'

    target_submenus_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    target_submenus_title = Column(String(50), unique=True)
    target_submenus_description = Column(Text)
    menus_id = Column(UUID(as_uuid=True), ForeignKey("menus.target_menus_id", ondelete='CASCADE'), nullable=True)


class Dishes(Base):
    __tablename__ = 'dishes'

    target_dishes_id = Column(UUID(as_uuid=True), primary_key=True, nullable=False,
                default=uuid.uuid4)
    target_dishes_title = Column(String(50), unique=True)
    target_dishes_description = Column(Text)
    target_dishes_price = Column(String(50))
    submenus_id = Column(UUID(as_uuid=True), ForeignKey('submenus.target_submenus_id', ondelete='CASCADE'), nullable=True)


