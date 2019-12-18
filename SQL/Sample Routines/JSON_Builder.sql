--General Details tab
--Plant and Work Tab
--Confined Space tab
--documents Tab
--Transitions
				
IF OBJECT_ID('tempdb..#tempConfig') IS NOT NULL  
begin
	drop table #tempConfig
end
Create table #tempConfig
(
	Stateconfigs nvarchar(100) collate Latin1_General_CI_AS,	   
	FromStateId nvarchar(100) collate Latin1_General_CI_AS,	   
	ToStateId nvarchar(100) collate Latin1_General_CI_AS,	   
	PermitOrApplicationTypeID int,
	ScreenOrTransition nvarchar(100) collate Latin1_General_CI_AS,	   
	Name nvarchar(100) collate Latin1_General_CI_AS,	   
	IsRequired nvarchar(100) collate Latin1_General_CI_AS,	   
	IsVisible nvarchar(100) collate Latin1_General_CI_AS,	   
	IsDisabled nvarchar(100) collate Latin1_General_CI_AS,	     
	DisplayPage nvarchar(100) collate Latin1_General_CI_AS,	     
)

insert into #tempConfig(			
Stateconfigs        
									,PermitOrApplicationTypeID
											,FromStateId
													,ToStateId
															,ScreenOrTransition
																						,Name
																																	,IsRequired
																																				,IsVisible
																																							,IsDisabled
																																										,DisplayPage) values

--Permit Request
------------------------------------------------------------------------------------------------------
--General Details tab
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'false'	,''			,''),


('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'Title'									,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkOrderNumber'							,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn7'					,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn8'					,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'ResponsibilityGroupName'					,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkGroupName'							,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'OutageID'									,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'TrainID'									,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'DirectionalityID'							,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn3'					,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn4'					,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'RequiredDateTime'							,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'Hira'										,''			,''			,'false'	,''),
('ApplicationStateConfigs'			,'5'	,'1'	,''		,'ScreenObjectConfigs'		,'PlantItems'								,''			,''			,'false'	,''),


--PTW
------------------------------------------------------------------------------------------------------
--General Details tab
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'Title'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkOrderNumber'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn7'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn8'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'ResponsibilityGroupName'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkGroupName'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'OutageID'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'TrainID'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'DirectionalityID'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn3'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn4'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn5'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'RequiredDateTime'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'ExpectedSurrenderDateTime'				,'false'	,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'Hira'										,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'PlantItems'								,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'EquipmentPrep'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'EpasEquipmentPrep'						,''			,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'PermitRelationships'						,''			,'true'		,'false'	,''),
--make both required and editable in planning approved state
('PermitStateConfigs'				,'3'	,'22'	,''		,'ScreenObjectConfigs'		,'RequiredDateTime'							,'true'		,''			,'false'	,''),
('PermitStateConfigs'				,'3'	,'22'	,''		,'ScreenObjectConfigs'		,'ExpectedSurrenderDateTime'				,'true'		,''			,'false'	,''),

('PermitStateConfigs'				,'3'	,'1'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'21'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'42'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'22'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'7'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'true'	    ,''),
('PermitStateConfigs'				,'3'	,'10'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'true'	    ,''),
-- permit documents
('PermitStateConfigs'				,'3'	,'7'	,''		,'ScreenObjectConfigs'		,'PermitDocs'								,''			,'true'		,'true'		,''),
--gas tests
('PermitStateConfigs'				,'3'	,'21'	,''		,'ScreenObjectConfigs'		,'InitialGasTestDateTime'					,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'21'	,''		,'ScreenObjectConfigs'		,'TestedByPersonID'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'3'	,'21'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'true'		,'false'	,''),
--transitions
('PermitStateTransitionConfigs'		,'3'	,'22'	,'7'	,'TransitionObjectConfigs'	,'Approvals'								,'true' 	,'true'		,'false'	,'1'),
('PermitStateTransitionConfigs'		,'3'	,'22'	,'7'	,'TransitionObjectConfigs'	,'PersonLookupFreeText'						,'true' 	,'true'		,'false'	,'2'),
('PermitStateTransitionConfigs'		,'3'	,'22'	,'6'	,'TransitionObjectConfigs'	,'PersonLookupFreeText'						,'true' 	,'true'		,'false'	,'1'),
('PermitStateTransitionConfigs'		,'3'	,'7'	,'10'	,'TransitionObjectConfigs'	,'Approvals'								,''			,'true'		,''			,'1'),
('PermitStateTransitionConfigs'		,'3'	,'7'	,'10'	,'TransitionObjectConfigs'	,'Notes'									,'true' 	,'true'		,'false'	,'2'),
('PermitStateTransitionConfigs'		,'3'	,'7'	,'10'	,'TransitionObjectConfigs'	,'PermitQuestionAnswers'					,'true' 	,'true'		,'false'	,'3'),
('PermitStateTransitionConfigs'		,'3'	,'1'	,'21'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,''),
('PermitStateTransitionConfigs'		,'3'	,'42'	,'22'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,''),
('PermitStateTransitionConfigs'		,'3'	,'7'	,'12'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,'1'),
('PermitStateTransitionConfigs'		,'3'	,'7'	,'12'	,'TransitionObjectConfigs'	,'Notes'									,''			,'true'		,''			,'2'),
('PermitStateTransitionConfigs'		,'3'	,'7'	,'12'	,'TransitionObjectConfigs'	,'PermitQuestionAnswers'					,'true' 	,'true'		,'false'	,'3'),

--CSEP
------------------------------------------------------------------------------------------------------
--General Details tab
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'Title'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'ResponsibilityGroupName'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'OutageID'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkLocation'								,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'TrainID'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'DirectionalityID'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn4'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn5'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkGroupLeader'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'SafetyObserver'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'Hira'										,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'PlantItems'								,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'EquipmentPrep'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'EpasEquipmentPrep'						,''			,''			,'false'	,''),
-- permit documents
('PermitStateConfigs'				,'8'	,'7'	,''		,'ScreenObjectConfigs'		,'PermitDocs'								,''			,'true'		,'true'		,''),
--gas tests
('PermitStateConfigs'				,'8'	,'21'	,''		,'ScreenObjectConfigs'		,'InitialGasTestDateTime'					,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'21'	,''		,'ScreenObjectConfigs'		,'TestedByPersonID'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'21'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'1'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'21'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'42'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'22'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'8'	,'7'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'true'	    ,''),
('PermitStateConfigs'				,'8'	,'10'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'true'	    ,''),

--transitions
('PermitStateTransitionConfigs'		,'8'	,'1'	,'21'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,''),
('PermitStateTransitionConfigs'		,'8'	,'42'	,'22'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,''),
('PermitStateTransitionConfigs'		,'8'	,'22'	,'7'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,''),
('PermitStateTransitionConfigs'		,'8'	,'7'	,'10'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,'1'),
('PermitStateTransitionConfigs'		,'8'	,'7'	,'10'	,'TransitionObjectConfigs'	,'Notes'									,'true'		,'true'		,'false'	,'2'),
('PermitStateTransitionConfigs'		,'8'	,'7'	,'12'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,'1'),
('PermitStateTransitionConfigs'		,'8'	,'7'	,'12'	,'TransitionObjectConfigs'	,'Notes'									,''			,'true'		,''			,'2'),
('PermitStateTransitionConfigs'		,'8'	,'7'	,'12'	,'TransitionObjectConfigs'	,'PermitQuestionAnswers'					,'true' 	,'true'		,'false'	,'3'),


--Blanket Permit
------------------------------------------------------------------------------------------------------
--General Details tab
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'Title'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn8'					,''			,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'ResponsibilityGroupName'					,'true'		,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'OutageID'									,''			,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'TrainID'									,'true'		,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'DirectionalityID'							,''			,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkOrderNumber'							,'false'	,'false'	,'true'		,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'Company'									,'false'	,'false'	,'true'		,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'WorkGroupName'							,'false'	,'false'	,'true'		,''),

('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn3'					,'false'	,'false'	,'true'		,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn4'					,'false'	,'false'	,'true'		,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'AdditionalTextColumn5'					,'false'	,'false'	,'true'		,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'EquipmentPrep'							,'false'	,'false'	,'true'		,''),

('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'RequiredDateTime'							,'true'		,''			,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'ExpectedSurrenderDateTime'				,'false'	,'false'	,'true'		,''),
--plant and work tab
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'PlantWorkTextArea1'					    ,''	        ,'true'	    ,'false'    ,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,'false'	,'false'	,''	        ,''),
('PermitStateConfigs'				,'51'	,'21'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,'false'	,'false'	,''	        ,''),
('PermitStateConfigs'				,'51'	,'42'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,'false'	,'false'	,''	        ,''),
('PermitStateConfigs'				,'51'	,'22'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,'false'	,'false'	,''	        ,''),
('PermitStateConfigs'				,'51'	,'7'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,'false'	,'false'	,''	        ,''),
('PermitStateConfigs'				,'51'	,'10'	,''		,'ScreenObjectConfigs'		,'JobDescription'							,'false'	,'false'	,''	        ,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'21'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'42'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'22'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'7'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'true'	    ,''),
('PermitStateConfigs'				,'51'	,'10'	,''		,'ScreenObjectConfigs'		,'GeneralDetailsTextArea2'					,'false'	,'true'		,'true'	    ,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'Hira'										,'true'		,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'1'	,''		,'ScreenObjectConfigs'		,'PlantItems'								,''			,''			,'false'	,''),
--make both required and editable in planning approved state
('PermitStateConfigs'				,'51'	,'22'	,''		,'ScreenObjectConfigs'		,'RequiredDateTime'							,'true'		,'true'		,'false'	,''),
-- permit documents
('PermitStateConfigs'				,'51'	,'7'	,''		,'ScreenObjectConfigs'		,'PermitDocs'								,''			,'true'		,'true'		,''),

--gas tests
('PermitStateConfigs'				,'51'	,'21'	,''		,'ScreenObjectConfigs'		,'InitialGasTestDateTime'					,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'21'	,''		,'ScreenObjectConfigs'		,'TestedByPersonID'							,''			,'true'		,'false'	,''),
('PermitStateConfigs'				,'51'	,'21'	,''		,'ScreenObjectConfigs'		,'PermitGasTests'							,''			,'true'		,'false'	,''),

--transitions
('PermitStateTransitionConfigs'		,'51'	,'22'	,'7'	,'TransitionObjectConfigs'	,'Approvals'								,'true' 	,'true'		,'false'	,'1'),
('PermitStateTransitionConfigs'		,'51'	,'7'	,'10'	,'TransitionObjectConfigs'	,'Approvals'								,''			,'true'		,''			,'1'),
('PermitStateTransitionConfigs'		,'51'	,'7'	,'10'	,'TransitionObjectConfigs'	,'Notes'									,'true' 	,'true'		,'false'	,'2'),
('PermitStateTransitionConfigs'		,'51'	,'7'	,'12'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,'1'),
('PermitStateTransitionConfigs'		,'51'	,'7'	,'12'	,'TransitionObjectConfigs'	,'Notes'									,''			,'true'		,''			,'2'),
('PermitStateTransitionConfigs'		,'51'	,'7'	,'12'	,'TransitionObjectConfigs'	,'PermitQuestionAnswers'					,'true' 	,'true'		,'false'	,'3'),
('PermitStateTransitionConfigs'		,'51'	,'1'	,'21'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,''),
('PermitStateTransitionConfigs'		,'51'	,'42'	,'22'	,'TransitionObjectConfigs'	,'Approvals'								,'' 		,'true'		,''			,'')


IF OBJECT_ID('tempdb..#Config') IS NOT NULL  
begin
	drop table #Config
end
Create table #Config
(
	id int identity,
	Stateconfigs nvarchar(100) collate Latin1_General_CI_AS,	   
	FromStateId nvarchar(100) collate Latin1_General_CI_AS,	   
	ToStateId nvarchar(100) collate Latin1_General_CI_AS,	   
	PermitOrApplicationTypeID int,
	ScreenOrTransition nvarchar(100) collate Latin1_General_CI_AS,	   
	Name nvarchar(100) collate Latin1_General_CI_AS,	   
	IsRequired nvarchar(100) collate Latin1_General_CI_AS,	   
	IsVisible nvarchar(100) collate Latin1_General_CI_AS,	   
	IsDisabled nvarchar(100) collate Latin1_General_CI_AS,	     
	DisplayPage nvarchar(100) collate Latin1_General_CI_AS	     
)
insert into #Config
select distinct
	*
from #tempConfig
order by Stateconfigs asc,PermitOrApplicationTypeID,FromStateId,ToStateId,ScreenOrTransition,name

declare @Stateconfigs_old               as nvarchar(255) = ''
declare @FromStateId_old                as nvarchar(255) = ''
declare @ToStateId_old                  as nvarchar(255) = ''
declare @PermitOrApplicationTypeID_old  as nvarchar(255) = ''
declare @ScreenOrTransition_old         as nvarchar(255) = ''
declare @Name_old                       as nvarchar(255) = ''
declare @IsRequired_old                 as nvarchar(255) = ''
declare @IsVisible_old                  as nvarchar(255) = ''
declare @IsDisabled_old                 as nvarchar(255) = ''
declare @DisplayPage_old                as nvarchar(255) = ''

declare @Stateconfigs                   as nvarchar(255) = ''
declare @FromStateId                    as nvarchar(255) = ''
declare @ToStateId                      as nvarchar(255) = ''
declare @PermitOrApplicationTypeID      as nvarchar(255) = ''
declare @ScreenOrTransition             as nvarchar(255) = ''
declare @Name                           as nvarchar(255) = ''
declare @IsRequired                     as nvarchar(255) = ''
declare @IsVisible                      as nvarchar(255) = ''
declare @IsDisabled                     as nvarchar(255) = ''
declare @DisplayPage                    as nvarchar(255) = ''

declare @Stateconfigs_next              as nvarchar(255) = ''
declare @FromStateId_next               as nvarchar(255) = ''
declare @ToStateId_next					as nvarchar(255) = ''
declare @PermitOrApplicationTypeID_next as nvarchar(255) = ''
declare @ScreenOrTransition_next        as nvarchar(255) = ''
declare @Name_next                      as nvarchar(255) = ''
declare @IsRequired_next                as nvarchar(255) = ''
declare @IsVisible_next                 as nvarchar(255) = ''
declare @IsDisabled_next                as nvarchar(255) = ''
declare @DisplayPage_next               as nvarchar(255) = ''

declare @String						    as nvarchar(max) = ''
declare @Count						    as int           = 1
declare @End						    as int           = (select Count(*) from #Config)

while @count<=(select Count(*) from #Config)
	begin
	

	------------------------------------------------------------------------------------------------------
	
	set @Stateconfigs_old               =@Stateconfigs
	set @FromStateId_old                =@FromStateId
	set @ToStateId_old                  =@ToStateId
	set @ToStateId_old                  =@ToStateId
	set @PermitOrApplicationTypeID_old  =@PermitOrApplicationTypeID
	set @ScreenOrTransition_old         =@ScreenOrTransition
	set @Name_old                       =@Name
	set @IsRequired_old                 =@IsRequired
	set @IsVisible_old                  =@IsVisible
	set @IsDisabled_old                 =@IsDisabled  
	set @DisplayPage_old                =@DisplayPage  

	set @Stateconfigs                   =(select Stateconfigs              from #Config where id=@count)                                    
	set @FromStateId                    =(select FromStateId               from #Config where id=@count)                               
	set @ToStateId                      =(select ToStateId                 from #Config where id=@count)                               
	set @PermitOrApplicationTypeID      =(select PermitOrApplicationTypeID from #Config where id=@count)                                                 
	set @ScreenOrTransition             =(select ScreenOrTransition        from #Config where id=@count)                                          
	set @Name                           =(select Name                      from #Config where id=@count)                            
	set @IsRequired                     =(select IsRequired                from #Config where id=@count)                                  
	set @IsVisible                      =(select IsVisible                 from #Config where id=@count)                                 
	set @IsDisabled                     =(select IsDisabled                from #Config where id=@count) 
	set @DisplayPage                    =(select DisplayPage               from #Config where id=@count) 
	
	set @Stateconfigs_next              =iif(@Count=@end,'',(select Stateconfigs              from #Config where id=@count+1))
	set @FromStateId_next               =iif(@Count=@end,'',(select FromStateId               from #Config where id=@count+1))
	set @ToStateId_next                 =iif(@Count=@end,'',(select ToStateId                 from #Config where id=@count+1))
	set @PermitOrApplicationTypeID_next =iif(@Count=@end,'',(select PermitOrApplicationTypeID from #Config where id=@count+1))
	set @ScreenOrTransition_next        =iif(@Count=@end,'',(select ScreenOrTransition        from #Config where id=@count+1))
	set @Name_next                      =iif(@Count=@end,'',(select Name                      from #Config where id=@count+1))
	set @IsRequired_next                =iif(@Count=@end,'',(select IsRequired                from #Config where id=@count+1))
	set @IsVisible_next                 =iif(@Count=@end,'',(select IsVisible                 from #Config where id=@count+1))
	set @IsDisabled_next                =iif(@Count=@end,'',(select IsDisabled                from #Config where id=@count+1))   
	set @DisplayPage_next               =iif(@Count=@end,'',(select DisplayPage               from #Config where id=@count+1))  
	
	if @Count=1
	set @string=@string+'{
'
------------------------------------------------------------------------------------------------------
	if @Stateconfigs<>@Stateconfigs_old                           
	set @string=@string+'    "'+@Stateconfigs+'": [		
'
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
	if @Fromstateid<>@FromStateId_old or @ToStateId<>@ToStateId_old or @PermitOrApplicationTypeID<>@PermitOrApplicationTypeID_old or @ScreenOrTransition<>@ScreenOrTransition_old
	set @string=@string+'		{
			'+iif(@tostateid='','"StateID": ','"FromStateID": ')+@FromStateId+',
			'+iif(@ToStateID<>'','"ToStateID": '+@ToStateId+',
			','')+'"PermitOrApplicationTypeID": '+@PermitOrApplicationTypeID+',
			"'+@ScreenOrTransition+'": [
'	
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
	set @string=@string+'				{
					"Name": "'+@Name+'"'+
					+iif(@IsRequired<>'',',
					"IsRequired": '+@IsRequired,'')
					+iif(@IsVisible<>'',',
					"IsVisible": '+@IsVisible,'')
					+iif(@IsDisabled<>'',',
					"IsDisabled": '+@IsDisabled,'')
					+iif(@DisplayPage<>'',',
					"DisplayPage": '+@DisplayPage,'')+'
				}'+iif(@Fromstateid=@FromStateId_next and @ToStateId=@ToStateId_next and @PermitOrApplicationTypeID=@PermitOrApplicationTypeID_next and @ScreenOrTransition=@ScreenOrTransition_next ,',','')+'
'
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
	if @Fromstateid<>@FromStateId_next or @ToStateId<>@ToStateId_next or @PermitOrApplicationTypeID<>@PermitOrApplicationTypeID_next or @ScreenOrTransition<>@ScreenOrTransition_next
	set @string=@string+'			]
		}'+iif(@Stateconfigs=@Stateconfigs_next,',','')+'
'	
------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------
	if @Stateconfigs<>isnull(@Stateconfigs_next,'')
	set @string=@string+'	]'+iif(@count<>@end,',','')+'
'
------------------------------------------------------------------------------------------------------
	if @Count=@end
	set @string=@string+'}
'


	if @count<>1
	set @string=substring(@string,2,10000)
	print @string
	set @string=right(@string,1)
	set @count=@count+1


	end
