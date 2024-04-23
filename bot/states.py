from config.fsm_factory import FSMSingleFactory

StartFSM = FSMSingleFactory("StartFSM", "start")

CompetitionFSM = FSMSingleFactory("CompetitionFSM", "main")
