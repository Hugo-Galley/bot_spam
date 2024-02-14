from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def spam_insta(id,pwd,victime,message,nbr_message):
    driver = webdriver.Chrome()
    driver.get("https://instagram.com")

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, '_a9--') and contains(@class, '_ap36') and contains(@class, '_a9_0')]")))

    bouton = driver.find_element(By.XPATH, "//button[contains(@class, '_a9--') and contains(@class, '_ap36') and contains(@class, '_a9_0')]")
    bouton.click()

    id_enter = driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
    id_enter.clear()
    id_enter.send_keys(id)
    time.sleep(2)

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='Mot de passe']")))

    id_pwd = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Mot de passe']")
    id_pwd.clear()
    id_pwd.send_keys(pwd)

    id_pwd.send_keys(Keys.RETURN)
    time.sleep(7)

    bouton_plus_tard = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37")))
    bouton_plus_tard.click()
    time.sleep(2)

    no_notif = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
    no_notif.click()
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    bouton_recherche = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.x1i10hfl[href='/direct/inbox/']")))
    bouton_recherche.click()

    time.sleep(2)
    wait = WebDriverWait(driver, 10)
    bouton_nouveau_message = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".x1i10hfl.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.x6s0dn4.xjbqb8w.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x1ypdohk.x78zum5.xl56j7k.x1y1aw1k.x1sxyh0.xwib8y2.xurb0ha.xcdnw81")))
    bouton_nouveau_message.click()
    time.sleep(2)

    ajout_nom = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[2]/div/div[2]/input")
    ajout_nom.send_keys(victime)
    time.sleep(2)

    choix8nom = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[3]/div/label/div/input")
    choix8nom.click()
    time.sleep(1)

    ajout_discussion = driver.find_element(By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[4]/div")
    ajout_discussion.click()
    time.sleep(2)

    for i in range(nbr_message):
        time.sleep(0.5)
        ajout_message = driver.find_element(By.CSS_SELECTOR, '.xzsf02u.x1a2a7pz.x1n2onr6.x14wi4xw.x1iyjqo2.x1gh3ibb.xisnujt.xeuugli.x1odjw0f')
        ajout_message.send_keys(message)
        time.sleep(0.5)
        envoyer_message =driver.find_element(By.CSS_SELECTOR,'.x1i10hfl.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.xdl72j9.x2lah0s.xe8uvvx.xdj266r.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x1lku1pv.x1a2a7pz.x6s0dn4.xjyslct.x1ejq31n.xd10rxx.x1sy0etr.x17r0tee.x9f619.x1ypdohk.x1f6kntn.xwhw2v2.xl56j7k.x17ydfre.x2b8uid.xlyipyv.x87ps6o.x14atkfc.xcdnw81.x1i0vuye.xjbqb8w.xm3z3ea.x1x8b98j.x131883w.x16mih1h.x972fbf.xcfux6l.x1qhh985.xm0m39n.xt0psk2.xt7dq6l.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x1n5bzlp.x173jzuc.x1yc6y37.xfs2ol5')
        envoyer_message.click()


input("Cliquer pour fermer la fenetre")