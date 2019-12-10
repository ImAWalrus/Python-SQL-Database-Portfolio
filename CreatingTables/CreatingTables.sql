DROP TABLE IF EXISTS 'Project';
create table 'Project'(
  pk int not null,
  Title varchar(100),
  Description varchar(100),
  Creation int,
  Project_id int,
  primary key (pk)
);

DROP TABLE IF EXISTS 'Tasks';
create table 'Tasks'(
  pk int not null,
  Title varchar(100),
  Description varchar(100),
  Time2Complete int,
  Task_id int,
  primary key (pk)
);

DROP TABLE IF EXISTS 'TaskAssocitation';
create table 'TaskAssocitation'(
  pk int not null,
  TaskAssco_id int,
  Preperation varchar(100),
  Implementaion varchar(100),
  Deployment varchar(100),
  Analysis varchar(100),
  primary key (pk)
);


DROP TABLE IF EXISTS 'Research';
create table 'Research'(
  pk int not null,
  Member_id int,
  name varchar(100),
  primary key (pk)
);

DROP TABLE IF EXISTS 'Owner';
create table 'Owner'(
  pk int not null,
  Owner_id int,
  workProject_id int,
  primary key (pk)
  --foreign key (Owner_id) references (workProject_id)
);

DROP TABLE IF EXISTS 'Metadata';
create table 'Metadata'(
  pk int not null,
  type varchar(100),
  title varchar(100),
  data varchar(100),
  Metadata_id int,
  primary key (pk),
  foreign key(type) references Project(pk)
);

DROP TABLE IF EXISTS 'Manage';
create table 'Manage'(
  pk int not null,
  task_id int,
  taskAssco_id int,
  project_id int,
  member_id int,
  owner_id int,
  metadata_id int,
  foreign key (task_id) references Tasks(pk),
  foreign key (taskAssco_id) references TaskAssocitation(pk),
  foreign key (project_id)  references Project(pk),
  foreign key (member_id) references Owner(pk),
  foreign key  (metadata_id) references Metadata (pk)
);
