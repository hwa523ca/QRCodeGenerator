import pygame, pygame_gui, qrcode, sys

pygame.init()

WIDTH, HEIGHT = 1200, 750
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("QR Code Generator")

CLOCK = pygame.time.Clock()
MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
font = pygame.font.Font("BebasNeue-Regular.ttf", 32)
inst1 = font.render("Type or paste the link:", True, "black", "white")
inst1_rect = inst1.get_rect()
inst1_rect.midleft = (175, 250)
TEXT_INPUT1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((175, 275), (900, 50)), manager=MANAGER,
                                                                            object_id="#main_text_entry")
inst2 = font.render("Type the name of the file, then press enter to generate it:", True, "black", "white")
inst2_rect = inst2.get_rect()
inst2_rect.midleft = (175, 425)
TEXT_INPUT2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((175, 450), (900, 50)), manager=MANAGER,
                                                                            object_id="#main_text_entry2")

def make_qr_code(link_name="https://www.youtube.com/channel/UC6tvRHEX2owW_1eb5Xb-o_A/", file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4
    )

    qr.add_data(link_name)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")

    if ".png" not in file_name:
        file_name += ".png"

    img.save(file_name)

def get_qr_code():
    link = ""
    while True:
        UI_REFRESH_RATE = CLOCK.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
                link = event.text

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry2":
                make_qr_code(TEXT_INPUT1.text, TEXT_INPUT2.text)
            
            MANAGER.process_events(event)
        MANAGER.update(UI_REFRESH_RATE)
        SCREEN.fill("white")
        SCREEN.blit(inst1, inst1_rect)
        SCREEN.blit(inst2, inst2_rect)
        MANAGER.draw_ui(SCREEN)

        pygame.display.update()

get_qr_code()