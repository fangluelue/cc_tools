import cc_data
import sys
import json

def make_optional_field_from_json(optional_fields):
    cc_level = cc_data.CCLevel()
    for field in optional_fields:
        if field["type"] == cc_data.CCMapTitleField.TYPE:
            CC_title = cc_data.CCMapTitleField(field["title"])
        elif field["type"] == cc_data.CCTrapControlsField.TYPE:
            TrapFields = []
            for trap in field["traps"]:
                bx = trap[1]
                by = trap[2]
                tx = trap[3]
                ty = trap[4]
                trapfield = cc_data.CCTrapControl(bx, by, tx, ty)
                TrapFields.append(trapfield)
            CC_TrapFields = cc_data.CCTrapControlsField(TrapFields)
        elif field["type"] == cc_data.CCCloningMachineControlsField.TYPE:
            CloFields = []
            for clone in field["Cloning"]:
                bx = clone[1]
                by = clone[2]
                tx = clone[3]
                ty = clone[4]
                clonefield = cc_data.CCCloningMachineControl(bx, by, tx, ty)
                CloFields.append(clonefield)
            CC_CloneMachine = cc_data.CCCloningMachineControlsField(CloFields)
        elif field["type"] == cc_data.CCEncodedPasswordField.TYPE:
            passwrod = field["password"]
            CC_password = cc_data.CCEncodedPasswordField(passwrod)
        elif field["type"] == cc_data.CCMapHintField.TYPE:
            hint = field["hint"]
            CC_hint = cc_data.CCMapHintField(hint)
        elif field["type"] == cc_data.CCMonsterMovementField.TYPE:
            MonsterFields = []
            for monster in field["monsters"]:
                x = monster[1]
                y = monster[2]
                monsterfield = cc_data.CCCoordinate(x, y)
                MonsterFields.append(monsterfield)
            CC_Monsterfield = cc_data.CCMonsterMovementField(MonsterFields)
        cc_level.add_field(CC_title)
        cc_level.add_field(CC_TrapFields)
        cc_level.add_field(CC_CloneMachine)
        cc_level.add_field(CC_password)
        cc_level.add_field(CC_hint)
        cc_level.add_field(CC_Monsterfield)
        return cc_level.optional_fields




def make_level_from_json(json_data):
    cclevel = cc_data.CCLevel()
    cclevel.level_number = json_data["levelnum"]
    cclevel.time = json_data["time"]
    cclevel.num_chips = json_data["chips"]
    cclevel.upper_layer = json_data["upper"]
    cclevel.lower_layer = json_data["lower"]
    cclevel.optional_fields = make_optional_field_from_json(json_data["optional_fields"])
    return cclevel

def make_cc_file_from_json(json_data):
    CC_dat = cc_data.CCDataFile();
    for level in json_data:
        CC_dat.add_level(make_level_from_json(level))
    return CC_dat

with open("luef_cc1.json", 'r') as reader:
    json_data = json.load(reader)

for level in json_data:
        print(level[1])

CC_data_file = make_cc_file_from_json(json_data)


